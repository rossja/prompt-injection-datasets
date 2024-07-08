# Prompt Injection Datasets

This repository contains lists of datasets that can be used to train
prompt defense or attack models.

It also contains some scripts to facilitate acquiring the datasets and
cleaning them up for use.

The datasets are listed in [dataset_list.csv](./dataset_list.csv) which
has the following structure:

```
src, url
```

The `src` identifies the type of dataset a source is:

* `od`: Open Dataset
* `hf`: HuggingFace Dataset
* `web`: Web based Dataset


## current status

This is still a work in progress but:

* The downloader works
* The dedupe works

There's a middle step of taking the downloaded data and putting it all into
a single csv that's missing from the automation (I've been doing that bit
manually for now). 
