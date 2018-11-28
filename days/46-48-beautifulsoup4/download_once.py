import os.path

import requests


def download_once(url, path, force_download=False):
    if not force_download and os.path.isfile(path):
        print("No file downloaded")
        return
    r = requests.get(url)
    r.raise_for_status()
    print("File downloaded")
    with open(path, "w+") as f:
        f.write(r.text)


def open_or_download(url, path, force_download=False):
    download_once(url, path, force_download)
    with open(path, "r") as f:
        text = f.read()
    return text
