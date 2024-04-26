from typing import Optional, Type

from src.common.database.curd import Curd
from src.common.database.model import MMD, Tag
from src.core.enums import DownloadStatus, Status
from src.utils.time_manager import get_current_datetime


class Service:
    def __init__(self):
        self._curd = Curd()

    def get_mmd(self, limit: Optional[int] = None, offset: Optional[int] = None) -> list[Type[MMD]]:
        return self._curd.get_mmd_query().limit(limit).offset(offset).all()

    def get_tag(self, limit: Optional[int] = None, offset: Optional[int] = None) -> list[Type[Tag]]:
        return self._curd.get_tag_query().limit(limit).offset(offset).all()

    def get_mmd_count(self) -> int:
        return self._curd.get_mmd_query().count()

    def get_tag_count(self) -> int:
        return self._curd.get_tag_query().count()

    def set_mmd_status(self, mmd_id: int, status: Status):
        self._curd.update_by_mmd_id(mmd_id, status=status.value)
        self._curd.update_by_mmd_id(mmd_id, update_time=get_current_datetime())

    def set_mmd_download_status(self, mmd_id: int, download_status: DownloadStatus):
        self._curd.update_by_mmd_id(mmd_id, download_status=download_status.value)
        self._curd.update_by_mmd_id(mmd_id, update_time=get_current_datetime())
