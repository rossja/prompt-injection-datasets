# Prompt Injection Datasets

This repository catalogs prompt injection, jailbreak, and general AI safety
datasets for training and evaluating attack and defense models.

The scope includes injection payloads and contexts, jailbreak prompts, harmful
requests, and labeled safety examples, including benign controls. General safety
datasets can supply the behaviors an attack attempts to elicit, such as CBRNE
content or hate speech. These are useful attack targets even when the examples
do not themselves contain a prompt injection or jailbreak.

It also contains some scripts to facilitate acquiring the datasets and
cleaning them up for use.

The datasets are listed in [dataset_list.csv](./dataset_list.csv) which
has the following structure:

```
src,url,license
```

The `src` identifies the type of dataset a source is:

* `kg`: Kaggle Dataset
* `hf`: HuggingFace Dataset
* `gh`: GitHub repository
* `web`: Web based Dataset

The `license` column records license metadata (blank means unspecified); the
downloader currently uses only `src` and `url`.

Kaggle sources (`kg`) use `opendatasets`. GitHub sources (`gh`) require Git on
`PATH` and an HTTPS repository URL such as `https://github.com/owner/repo`.
They are shallow clones of the default branch, saved under
`datasets/github/<owner>/<repo>`. Cloning reports an error if that destination
already exists and is nonempty. Use `web` for individual raw file URLs.

Run the source-format regression tests without downloading datasets:

```sh
uv run --no-project --with pandas python -m unittest discover -s tests -v
```

## Source selection

The [2026-09-15 research review](docs/dataset-research-2026-09-15.md) records
new sources, their roles, publisher evidence, known overlap, and excluded
mirrors. The catalog includes attack payloads, harmful-request seeds,
contextual benchmarks, safety labels, and benign controls.

The `license` field records declared data terms where established; a blank
means unspecified or unresolved. Some sources have mixed or custom terms,
noncommercial restrictions, evaluation-only intended use, or gated access.
See the review and publisher terms before acquiring or using a dataset.

Source selection avoids known mirrors, but individual examples across datasets
have not been deduplicated. Preserve source IDs, context and train/test splits
when extracting examples. Downloading a GitHub repository does not itself
extract its dataset from the surrounding code and benchmark files.

## current status

This is still a work in progress but:

* The downloader works
* The dedupe works

There's a middle step of taking the downloaded data and putting it all into
a single csv that's missing from the automation (I've been doing that bit
manually for now).
