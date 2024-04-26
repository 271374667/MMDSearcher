from typing import Optional

from src.common.database.service import Service
from src.core.config import DEFAULT_PAGE_SIZE
from src.backend.types.apifox import ApifoxModel


class HomeService:
    def __init__(self):
        self._service = Service()

    def get_mmd_count(self) -> int:
        return self._service.get_mmd_count()

    def get_tag_count(self) -> int:
        return self._service.get_tag_count()

    def get_mmd(self, limit: Optional[int] = DEFAULT_PAGE_SIZE, offset: Optional[int] = 0):
        mmd_list = self._service.get_mmd(limit=limit, offset=offset)
        return self._service.get_mmd(limit=limit, offset=offset)

    def get_all_tag(self):
        return self._service.get_tag()
