"""
用于初始化以及一些检查
"""
import json

import loguru

from src.common.database.session import create_db
from src.common.db_version_manager import create_db_meta
from src.core import config, paths
from src.core.settings import settings


def init_log() -> None:
    loguru.logger.add(paths.LOG_FILE, rotation=config.LOG_ROTATION, retention=config.LOG_RETENTION,
                      encoding=config.LOG_ENCODING)
    loguru.logger.success("日志初始化完成")


def create_all_dir_if_not_exists() -> None:
    for each in paths.ALL_DIRS:
        each.mkdir(parents=True, exist_ok=True)


def create_db_if_not_exists() -> None:
    if not paths.DATABASE_FILE.exists():
        create_db()
        loguru.logger.success("数据库文件创建完成")


def create_config_if_not_exists() -> None:
    if not paths.CONFIG_FILE.exists():
        settings.save()
        loguru.logger.success("配置文件创建完成")


def create_db_meta_if_not_exists() -> None:
    if not paths.DATABASE_META_FILE.exists():
        meta = create_db_meta()
        paths.DATABASE_META_FILE.write_text(json.dumps(meta, indent=2))
        loguru.logger.success("数据库元数据文件创建完成")


def pre_lunch() -> None:
    create_all_dir_if_not_exists()
    create_db_if_not_exists()
    create_config_if_not_exists()
    create_db_meta_if_not_exists()
    init_log()
    loguru.logger.success("初始化完成")


if __name__ == "__main__":
    pre_lunch()
