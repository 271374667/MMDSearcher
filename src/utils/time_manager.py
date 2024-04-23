"""
转换时间格式
时间格式: 2021-01-01 00:00:00

"""
from datetime import datetime


def str2datetime(datetime_str: str):
    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")


def datetime2str(datetime_obj: datetime):
    return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")


def get_current_datetime() -> datetime:
    return datetime.now()


def get_current_datetime_str() -> str:
    return datetime2str(get_current_datetime())
