"""
用于初始化以及一些检查
"""

import loguru

from src.core import config, paths


def init_log() -> None:
    loguru.logger.add(paths.LOG_FILE, rotation=config.LOG_ROTATION, retention=config.LOG_RETENTION,
                      encoding=config.LOG_ENCODING)
    loguru.logger.success("日志初始化完成")


def create_all_dir_if_not_exists() -> None:
    for each in paths.ALL_DIRS:
        each.mkdir(parents=True, exist_ok=True)


def pre_lunch() -> None:
    create_all_dir_if_not_exists()
    init_log()
    loguru.logger.success("初始化完成")


if __name__ == "__main__":
    pre_lunch()
