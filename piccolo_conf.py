from piccolo.engine import SQLiteEngine
from piccolo.conf.apps import AppRegistry
from src.config import database_path

DB = SQLiteEngine(path=database_path)


# def init_db():
#     try:
#         # Convert string path to Path object if necessary
#         path = Path(db_path)
#
#         # Check if file already exists
#         if path.exists():
#             logger.info(f"File already exists: {path}")
#             return None
#
#         # Create all intermediate directories
#         path.parent.mkdir(parents=True, exist_ok=True, mode=770)
#         path.touch()
#         logger.info(f"Successfully created file: {path}")
#
#         return
#
#     except PermissionError as e:
#         logger.error(f"Permission denied while creating {db_path}: {e}")
#         raise OSError(f"Permission denied: {e}")
#     except OSError as e:
#         logger.error(f"OS error while creating {db_path}: {e}")
#         raise OSError(f"Failed to create file: {e}")
#     except Exception as e:
#         logger.error(f"Unexpected error while creating {db_path}: {e}")
#         raise Exception(f"Unexpected error: {e}")
#
# database_inst = init_db()


APP_REGISTRY = AppRegistry(apps=["src.database.piccolo_app"])