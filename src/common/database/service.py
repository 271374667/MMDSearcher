from src.common.database.curd import Curd


class Service:
    def __init__(self):
        self._curd = Curd()

    def get_mmd_count(self) -> int:
        return self._curd.get_mmd_query().count()

    def get_tag_count(self) -> int:
        return self._curd.get_tag_query().count()
