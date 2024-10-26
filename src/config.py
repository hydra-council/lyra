import json
import os
from datetime import datetime
from functools import lru_cache
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


class JsonFormatter(logging.Formatter):
    """Custom JSON formatter for log records"""

    def format(self, record):
        # Base log record attributes
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = {
                "type": str(record.exc_info[0].__name__),
                "message": str(record.exc_info[1]),
                "traceback": self.formatException(record.exc_info)
            }

        # Add extra fields if present
        if hasattr(record, "extra_data"):
            log_data.update(record.extra_data)

        return json.dumps(log_data)


def setup_logger(log_dir: str, max_logs: int = 5, max_size: int = 1024 * 1024) -> logging.Logger:
    """
    Sets up a logger with human-readable console output and JSON file output.

    Args:
        log_dir: Directory to store log files (default: 'logs')
        max_logs: Maximum number of backup log files (default: 5)
        max_size: Maximum size of each log file in bytes (default: 1MB)

    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Clear any existing handlers
    logger.handlers = []

    # Create console handler with human-readable format
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    try:
        # Create logs directory if it doesn't exist
        Path(log_dir).mkdir(parents=True, exist_ok=True)

        # Create rotating file handler with JSON format
        log_file = os.path.join(log_dir, 'app.log')
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_size,
            backupCount=max_logs
        )
        file_handler.setFormatter(JsonFormatter())
        logger.addHandler(file_handler)

    except Exception as e:
        logger.error(f"Failed to setup file logging: {e}")
        logger.info("Continuing with console logging only")

    return logger

@lru_cache()
def get_env():
    port = 55001
    host = '0.0.0.0'
    addr = f"{host}:{port}"

    is_docker = os.getenv("IS_DOCKER")

    if is_docker is None:
        base_appdata = '../appdata'
        print("App is not running in docker")
    else:
        base_appdata = '/data/lyra'
        print("App is running in docker")

    database_path = f'{base_appdata}/lyra.db'
    repo_manifests = f'{base_appdata}/repo_manifests'
    extension_data = f'{base_appdata}/extension_data'
    logs = f'{base_appdata}/logs'

    os.makedirs(repo_manifests, exist_ok=True)
    os.makedirs(extension_data, exist_ok=True)
    os.makedirs(logs, exist_ok=True)

    return addr, base_appdata, database_path, repo_manifests, extension_data, logs

addr, base_appdata_dir, db_path, repo_manifest_dir, extension_data_dir, log_dir = get_env()

logger = setup_logger(log_dir)
