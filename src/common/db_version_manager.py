import hashlib
import json
from pathlib import Path
from typing import Optional

import loguru
import requests

from src.common.database.service import Service
from src.core.config import DATABASE_FILE_URL, DATABASE_META_URL, REMOTE_REPOSITORY
from src.core.paths import DATABASE_FILE, DATABASE_META_FILE
from src.utils.time_manager import get_current_datetime_str


def file2md5(file_path: Path) -> str:
    """计算文件的md5值

    Args:
        file_path (Path): 文件路径

    Returns:
        str: md5值
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def create_db_meta() -> dict:
    """创建数据库元数据文件

    格式如下:{'mmd_count': 0,'tag_count': 0, 'last_update_time': '2021-09-01 00:00:00', 'md5': 'xxx'}
    """
    s = Service()
    mmd_count = s.get_mmd_count()
    md5 = file2md5(DATABASE_FILE)
    tag_count = s.get_tag_count()
    return {'mmd_count': mmd_count, 'tag_count': tag_count, 'last_update_time': get_current_datetime_str(), 'md5': md5}


def get_db_meta() -> dict:
    """获取数据库元数据

    Returns:
        dict: 数据库元数据
    """
    with open(DATABASE_META_FILE, 'r') as f:
        return json.load(f)


def get_db_from_remote() -> Optional[dict]:
    """从远程仓库下载数据库文件"""
    loguru.logger.debug(f'开始从远程仓库{REMOTE_REPOSITORY}下载数据库文件')
    try:
        response = requests.get(DATABASE_META_URL).json()
        loguru.logger.debug('从远程仓库下载数据库文件成功')
        loguru.logger.debug(f'远程仓库数据库元数据: {response}')
    except Exception as e:
        loguru.logger.error(f'从远程仓库下载数据库文件失败, {e}')
        return None
    return response


def write_db_meta(meta: dict) -> None:
    """更新数据库元数据

    Args:
        meta (dict): 数据库元数据
    """
    with open(DATABASE_META_FILE, 'w') as f:
        json.dump(meta, f, indent=2)


def download_new_db_from_remote() -> None:
    """从远程仓库下载最新的数据库文件"""
    loguru.logger.debug(f'开始从远程仓库{REMOTE_REPOSITORY}下载数据库文件')
    try:
        response = requests.get(DATABASE_FILE_URL)
        with open(DATABASE_FILE_URL, 'wb') as f:
            f.write(response.content)
        loguru.logger.debug(f'从远程仓库下载数据库文件成功, 大小为{len(response.content) / (1024 * 1024):.2f}MB')
    except Exception as e:
        loguru.logger.error(f'从远程仓库下载数据库文件失败, {e}')


def is_db_meta_changed() -> bool:
    """判断数据库元数据是否发生变化

    Returns:
        bool: 是否发生变化
    """
    old_meta = get_db_from_remote()
    if not old_meta:
        return False
    new_meta = create_db_meta()
    current_md5 = file2md5(DATABASE_META_FILE)
    new_meta['md5'] = current_md5

    if old_meta['md5'] == new_meta['md5']:
        return False
    old_meta['md5'] = current_md5
    write_db_meta(new_meta)
    loguru.logger.debug(f'数据库元数据发生变化, {old_meta} -> {new_meta}')
    download_new_db_from_remote()
    return True


if __name__ == '__main__':
    # print(is_db_meta_changed())
    download_new_db_from_remote()
