from socket import fromfd

import requests
import json
import os
from database import *

manifest_dir = '.'

plugin_path = '../extensions'


def download_repo_manifest(repo_url: str) -> bool:
    """
    Downloads the repository manifest and validates its contents.

    Args:
        repo_url: URL to the repository manifest JSON

    Returns:
        bool: True if download and validation successful, False otherwise
    """
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
            'extensionsMetaDataUrls': list
        }

        # Validate all required fields exist and are of correct type
        for field, field_type in required_fields.items():
            if field not in manifest_data:
                print(f"Error: Missing required field '{field}' in manifest")
                return False
            if not isinstance(manifest_data[field], field_type):
                print(f"Error: Field '{field}' has incorrect type")
                return False

        # Save manifest to file
        manifest_path = os.path.join(manifest_dir, 'repo_manifest.json')
        with open(manifest_path, 'w') as f:
            json.dump(manifest_data, f, indent=2)

        print(f"Successfully downloaded and validated manifest to {manifest_path}")
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


def update_repo_manifest() -> None:
    """
    Updates the repository manifest by comparing the existing version
    with the remote version.
    """
    try:
        # Load existing manifest
        local_manifest_path = os.path.join(manifest_dir, 'repo_manifest.json')
        if not os.path.exists(local_manifest_path):
            print("No existing manifest found. Please download first.")
            return

        with open(local_manifest_path, 'r') as f:
            local_manifest = json.load(f)

        # Get remote manifest URL
        remote_url = local_manifest.get('jsonRepoUrl')
        if not remote_url:
            print("Error: No jsonRepoUrl found in local manifest")
            return

        # Download new manifest
        response = requests.get(remote_url)
        response.raise_for_status()
        remote_manifest = response.json()

        # Compare versions
        local_version = local_manifest.get('version')
        remote_version = remote_manifest.get('version')

        if not local_version or not remote_version:
            print("Error: Version information missing in manifest")
            return

        if remote_version > local_version:
            print(f"New version available: {remote_version} (current: {local_version})")
            # Save new manifest
            with open(local_manifest_path, 'w') as f:
                json.dump(remote_manifest, f, indent=2)
            print("Manifest updated successfully")
        else:
            print(f"Already at latest version ({local_version})")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading remote manifest: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing manifest JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def download_extension_manifest():
    pass


def update_extension_manifest():
    pass


# download_plugin('https://github.com/hydra-council/manga-extensions')
update_plugin('https://github.com/hydra-council/manga-extensions')
