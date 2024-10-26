import os
from os import makedirs
from pathlib import Path

from peewee import *
from playhouse.sqlite_ext import JSONField
from src.config import get_env, logger, db_path

database_inst = SqliteDatabase(db_path)

def init_db():
    try:
        # Convert string path to Path object if necessary
        path = Path(db_path)

        # Check if file already exists
        if path.exists():
            logger.info(f"File already exists: {path}")
            return None

        # Create all intermediate directories
        path.parent.mkdir(parents=True, exist_ok=True, mode=770)
        path.touch()
        logger.info(f"Successfully created file: {path}")

        database_inst.connect()

    except PermissionError as e:
        logger.error(f"Permission denied while creating {db_path}: {e}")
        raise OSError(f"Permission denied: {e}")
    except OSError as e:
        logger.error(f"OS error while creating {db_path}: {e}")
        raise OSError(f"Failed to create file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error while creating {db_path}: {e}")
        raise Exception(f"Unexpected error: {e}")


class ExtensionRepo(Model):
    repoName = TextField()
    repoUrl = TextField()
    jsonRepoUrl = TextField()
    version = TextField()
    repo_manifest_version = TextField()
    extensionsMetaDataUrls = JSONField()

    class Meta:
        database = database_inst


class Extension(Model):
    display_name = TextField()
    manifest_version = TextField()
    extension_version = TextField()
    media_type = TextField()
    repo_url = TextField()
    script_url = TextField()
    meta_data_url = TextField()
    file_url = TextField()
    extension_repo = ForeignKeyField(ExtensionRepo, backref='extensions')

    class Meta:
        database = database_inst