# function to get the name of a file from a url
def get_filename(url):
    from os import path
    fragment_removed = url.split("#")[0]  # keep to left of first #
    query_string_removed = fragment_removed.split("?")[0]
    scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
    if scheme_removed.find("/") == -1:
        return ""
    return path.basename(scheme_removed)

# function to download a dataset from the internet (especially kaggle) using opendatasets
def download_opendataset(dataset_url):
    import opendatasets as od
    try:
        od.download(dataset_url, data_dir="datasets")
        return("Dataset downloaded successfully")
    except Exception as e:
        return(e)

# # function to download a dataset from huggingface using huggingface_hub
# def download_hfdataset(repo_id, filename):
#     from huggingface_hub import hf_hub_download
#     try:
#         hf_hub_download(repo_id, filename)
#         return("Dataset downloaded successfully")
#     except Exception as e:
#         return(e)

# function to download a snapshot of a dataset from huggingface using huggingface_hub
def download_hfdataset(hfurl, repo_type="dataset"):
    import os
    repo_id = hfurl.split("https://huggingface.co/datasets/")[1]
    local_dir=os.path.join("datasets", repo_id)

    from huggingface_hub import snapshot_download
    try:
        snapshot_download(repo_id, repo_type=repo_type, local_dir=local_dir)
        return("Dataset downloaded successfully")
    except Exception as e:
        return(e)

# function to download a dataset from the internet using requests
def download_webdataset(url, filename=""):
    # set filename to the name of the file in the url if not provided
    if filename == "":
        filename = get_filename(url)

    import os
    data_file = os.path.join("datasets", filename)

    import requests
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(data_file, 'wb') as file:
            file.write(response.content)
        return("Dataset downloaded successfully")
    except Exception as e:
        return(e)

# parse the list.csv file to get the urls of the datasets to download
# then call the appropriate function to download the dataset
def download_datasets(list_csv_file):
    import pandas as pd
    df = pd.read_csv(list_csv_file)
    for index, row in df.iterrows():
        if row['src'] == 'od':
            print(download_opendataset(row['url']))
        elif row['src'] == 'hf':
            print(download_hfdataset(row['url']))
        elif row['src'] == 'web':
            print(download_webdataset(row['url']))
        else:
            print("Invalid source")
    return("All datasets downloaded successfully")

if __name__ == '__main__':
    # download the datasets listed in the dataset_list.csv file
    download_datasets("dataset_list.csv")