from enum import Enum
from typing import Union

from typing_extensions import Self


# 这一条记录的下载状态,0表示无法下载(比如链接失效,1表示可以下载,2代表未知网站
class DownloadStatus(Enum):
    CANNOT_DOWNLOAD = 0
    CAN_DOWNLOAD = 1
    UNKNOWN_WEBSITE = 2

    @classmethod
    def has_value(cls, download_status: Union[int, Self]) -> bool:
        keys, values = zip(*cls._value2member_map_.items())
        return download_status in keys or download_status in values

    @classmethod
    def values(cls) -> list[int]:
        return [item.value for item in cls]


# 这一条记录的状态,0表示还未看过,1表示已经看过
class Status(Enum):
    UNREAD = 0
    READ = 1

    @classmethod
    def has_value(cls, status: Union[int, Self]) -> bool:
        keys, values = zip(*cls._value2member_map_.items())
        return status in keys or status in values

    @classmethod
    def values(cls) -> list[int]:
        return [item.value for item in cls]


if __name__ == '__main__':
    print(DownloadStatus.has_value(1))
    print(DownloadStatus.has_value(DownloadStatus.CAN_DOWNLOAD))
