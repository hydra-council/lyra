import os

from git import Repo
from urllib.parse import urlparse

plugin_path = '../extensions'


def download_plugin(repo_link):
    parsed = urlparse(repo_link)
    path_parts = [part for part in parsed.path.split('/') if part]
    repo_owner, repo_name = path_parts[-2], (path_parts[-1]).rstrip('.git')
    return Repo.clone_from(repo_link, f'{plugin_path}/{repo_owner}_{repo_name}')


def delete_plugin():
    pass


def list_plugins():
    dirs = os.listdir(plugin_path)
    for dird in dirs:
        if os.path.isdir(dird):
        print(dird)

def update_plugin(repo_link):
    repo = Repo(repo_link)
    repo.remote('origin').fetch()

# download_plugin('https://github.com/hydra-council/manga-extensions')
list_plugins()