from datetime import datetime
from piccolo.table import Table, create_db_tables, create_db_tables_sync
from piccolo.columns import ForeignKey, Integer, Varchar, Timestamp, JSONB, Text


def init_database():
    create_db_tables_sync(ExtensionRepo, Extension, if_not_exists=True)


class ExtensionRepo(Table):
    repoName = Varchar(length=100)
    repoUrl = Text()
    jsonRepoUrl = Text(unique=True)
    version = Varchar(length=50)
    repo_manifest_version = Integer()
    modified_on = Timestamp(auto_update=datetime.now)


class Extension(Table):
    display_name = Varchar(length=100)
    manifest_version = Integer()
    extension_version = Varchar()
    media_type = Text()
    repo_url = Text()
    script_url = Text(unique=True)
    meta_data_url = Text()
    script_file_url = Text(unique=True)
    extension_repo = ForeignKey(ExtensionRepo, backref='extensions')
    modified_on = Timestamp(auto_update=datetime.now)
