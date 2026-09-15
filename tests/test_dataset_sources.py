"""Regression tests for dataset manifest sources and GitHub downloads."""

import contextlib
import csv
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

from src import downloader


class DatasetSourcesTest(unittest.TestCase):
    """Check source dispatch against fixtures and the current manifest."""

    def check_manifest(self, manifest):
        with contextlib.ExitStack() as stack:
            handlers = {
                source: stack.enter_context(mock.patch.object(downloader, name))
                for source, name in {
                    'kg': 'download_opendataset',
                    'hf': 'download_hfdataset',
                    'gh': 'download_ghdataset',
                    'web': 'download_webdataset',
                }.items()
            }
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            downloader.download_datasets(manifest)
            with open(manifest, encoding='utf-8', newline='') as source_file:
                rows = list(csv.DictReader(source_file))
            for source, handler in handlers.items():
                self.assertEqual(
                    handler.call_args_list,
                    [mock.call(row['url']) for row in rows
                     if row['src'] == source],
                )
            self.assertEqual(
                sum(handler.call_count for handler in handlers.values()),
                len(rows),
            )

    def test_current_manifest(self):
        self.check_manifest('dataset_list.csv')

    def test_all_sources_with_blank_and_populated_licenses(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / 'datasets.csv'
            with manifest.open('w', encoding='utf-8', newline='') as output:
                writer = csv.writer(output)
                writer.writerow(['src', 'url', 'license'])
                for source in ('kg', 'hf', 'gh', 'web'):
                    for license_name in ('', 'MIT'):
                        writer.writerow([
                            source, f'https://example.com/{source}',
                            license_name,
                        ])
            self.check_manifest(manifest)


class GithubDownloadTest(unittest.TestCase):
    """Check repository downloads without contacting GitHub."""

    def test_clone_default_branch_with_supported_url_forms(self):
        for suffix in ('', '/', '.git', '.git/'):
            with self.subTest(suffix=suffix), \
                 tempfile.TemporaryDirectory() as directory, \
                 mock.patch('src.downloader.Path', wraps=Path) as path_class, \
                 mock.patch('subprocess.run') as run:
                path_class.return_value = Path(directory) / 'datasets'
                url = f'https://github.com/owner/repository{suffix}'
                result = downloader.download_ghdataset(url)
                destination = (
                    Path(directory) / 'datasets/github/owner/repository'
                )
                self.assertTrue(destination.parent.is_dir())
                run.assert_called_once_with(
                    ['git', 'clone', '--depth', '1', '--', url,
                     str(destination)],
                    check=True,
                )
                self.assertEqual(result, 'Dataset downloaded successfully')

    def test_rejects_non_repository_urls(self):
        for url in (
            'https://example.com/owner/repo',
            'https://github.com/owner/repo/tree/main',
            'https://github.com/owner/..',
            'https://github.com/owner',
        ):
            with self.subTest(url=url), mock.patch('subprocess.run') as run:
                self.assertIsInstance(
                    downloader.download_ghdataset(url), ValueError
                )
                run.assert_not_called()

    def test_clone_errors_are_returned(self):
        for error in (FileNotFoundError('git'),
                      subprocess.CalledProcessError(128, 'git')):
            with self.subTest(error=error), \
                 mock.patch('pathlib.Path.mkdir'), \
                 mock.patch('subprocess.run', side_effect=error):
                self.assertIs(
                    downloader.download_ghdataset('https://github.com/o/r'),
                    error,
                )


if __name__ == '__main__':
    unittest.main()
