import platform

import requests
import json
import os

import uuid

from src.config import extension_data, logger
from src.database.tables import *


def validate_json(required_fields, manifest_data):
    # Validate all required fields exist and are of correct type
    for field, field_type in required_fields.items():
        if field not in manifest_data:
            print(f"Error: Missing required field '{field}' in manifest")
            return False
        if not isinstance(manifest_data[field], field_type):
            print(f"Error: Field '{field}' has incorrect type")
            return False
    return True


def download_repo_manifest(repo_url: str) -> bool:
    try:
        # Download the manifest
        response = requests.get(repo_url)
        response.raise_for_status()
        manifest_data = response.json()

        # Required fields in the manifest
        required_fields = {
            'repoName': str,
            'repoUrl': str,
            'jsonRepoUrl': str,
            'version': str,
            'manifest_version': int,
            'extensionsMetaDataUrls': list
        }

        validate = validate_json(required_fields, manifest_data)
        if validate is False:
            return False

        repo = ExtensionRepo(
            repoName=manifest_data["repoName"],
            repoUrl=manifest_data["repoUrl"],
            jsonRepoUrl=manifest_data["jsonRepoUrl"],
            version=manifest_data["version"],
            repo_manifest_version=manifest_data["manifest_version"],
        )

        res = repo.save().on_conflict(
            action="DO UPDATE",
            values=[
                ExtensionRepo.version,
                ExtensionRepo.repo_manifest_version,
                ExtensionRepo.repoName
            ]
        ).run_sync()

        for extension in manifest_data["extensionsMetaDataUrls"]:
            download_extension_manifest(extension, res[0]['id'])

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading manifest: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error parsing manifest JSON: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def download_extension_manifest(extension_url, extension_repo_id):
    try:
        # Download the manifest
        response = requests.get(extension_url)
        response.raise_for_status()
        manifest_data = response.json()

        # Required fields in the manifest
        required_fields = {
            "name": str,
            "manifest_version": int,
            "version": str,
            "media_type": str,
            "repoUrl": str,
            "scriptUrl": str,
            "metaDataUrl": str
        }

        validate = validate_json(required_fields, manifest_data)
        if validate is False:
            return False

        repo = Extension(
            display_name=manifest_data["name"],
            manifest_version=manifest_data["manifest_version"],
            extension_version=manifest_data["version"],
            media_type=manifest_data["media_type"],
            repo_url=manifest_data["repoUrl"],
            script_url=manifest_data["scriptUrl"],
            meta_data_url=manifest_data["metaDataUrl"],
            script_file_url='',  # indicate not installed status
            extension_repo=extension_repo_id
        )

        repo.save().on_conflict(
            action="DO UPDATE",
            values=[
                Extension.extension_version,
                Extension.manifest_version,
                Extension.display_name,
            ]).run_sync()

        print(f"Successfully downloaded and validated manifest")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading manifest: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error parsing manifest JSON: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def install_extension(ext_id):
    res = Extension.select(Extension.script_url).where(Extension.id == ext_id).run_sync()

    if len(res):
        url = res[0]['script_url']
        resp = requests.get(url)
        resp.raise_for_status()

        if resp.headers['Content-Type'] != 'text/plain; charset=utf-8':
            raise Exception(f'Content type must be text/plain; charset=utf-8 response content type: {resp.headers['Content-Type']}')


        ext_uuid = str(uuid.uuid4())

        # Create directory if it doesn't exist
        directory = os.path.join(extension_data, ext_uuid)
        if directory:
            os.makedirs(directory, exist_ok=True)

        filepath = os.path.join(directory, f'{url.split('/')[-1]}')

        # Write content to file
        with open(filepath, 'wb') as f:
            f.write(resp.content)

        if platform.system() == 'Windows':
            logger.warning('OS is detected as windows skipping chown and chmod')
            return True

        # Change ownership and permissions
        os.chown(filepath, 1000, 1000)
        os.chmod(filepath, 660)
        return True
    else:
        raise Exception(f"Could not find extension with id: {ext_id}")


def update_extension_manifest():
    pass

# install_extension(1)
# download_repo_manifest('https://raw.githubusercontent.com/hydra-council/manga-extensions/refs/heads/main/repo_manifest.json')
# update_plugin('https://github.com/hydra-council/manga-extensions')
