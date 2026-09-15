# Prompt Injection Datasets

This repository contains lists of datasets that can be used to train
prompt defense or attack models.

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

## current status

This is still a work in progress but:

* The downloader works
* The dedupe works

There's a middle step of taking the downloaded data and putting it all into
a single csv that's missing from the automation (I've been doing that bit
manually for now).
