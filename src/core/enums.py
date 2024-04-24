from enum import Enum


# 这一条记录的下载状态,0表示无法下载(比如链接失效,1表示可以下载,2代表未知网站
class DownloadStatus(Enum):
    CANNOT_DOWNLOAD = 0
    CAN_DOWNLOAD = 1
    UNKNOWN_WEBSITE = 2


# 这一条记录的状态,0表示还未看过,1表示已经看过
class Status(Enum):
    UNREAD = 0
    READ = 1
