from typing import Optional, Type

from sqlalchemy import and_, or_

from src.common.database.curd import Curd
from src.common.database.model import MMD, Tag
from src.core.datacls import ApifoxDataclass
from src.core.enums import DownloadStatus, Status
from src.utils.time_manager import get_current_datetime


class Service:
    def __init__(self):
        self._curd = Curd()

    def get_mmd(self, query_dataclass: ApifoxDataclass) -> list[Type[MMD]]:
        filters = []

        if query_dataclass.author is not None:
            filters.append(MMD.author.like(f"%{query_dataclass.author}%"))

        if query_dataclass.download_status is not None:
            filters.append(MMD.download_status == query_dataclass.download_status)

        if query_dataclass.mmd_id is not None:
            filters.append(MMD.mmd_id == query_dataclass.mmd_id)

        if query_dataclass.post_time_search_begin is not None and query_dataclass.post_time_search_end is not None:
            filters.append(
                    MMD.post_time.between(query_dataclass.post_time_search_begin, query_dataclass.post_time_search_end))

        if query_dataclass.rating is not None:
            filters.append(MMD.rating == query_dataclass.rating)

        if query_dataclass.score is not None:
            if query_dataclass.score_operation == 0:
                filters.append(MMD.score == query_dataclass.score)
            elif query_dataclass.score_operation == 1:
                filters.append(MMD.score < query_dataclass.score)
            elif query_dataclass.score_operation == 2:
                filters.append(MMD.score > query_dataclass.score)

        if query_dataclass.status is not None:
            filters.append(MMD.status == query_dataclass.status)

        if query_dataclass.tags is not None:
            tags = query_dataclass.tags.split('#')
            if query_dataclass.tag_operation == 0:
                filters.append(or_(*[MMD.tags.like(f"%{tag}%") for tag in tags]))
            elif query_dataclass.tag_operation == 1:
                filters.append(and_(*[MMD.tags.like(f"%{tag}%") for tag in tags]))

        return (self._curd.get_mmd_query()
                .filter(*filters)
                .limit(query_dataclass.limit)
                .offset(query_dataclass.offset)
                .all())

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
