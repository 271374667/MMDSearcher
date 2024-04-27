
from src.backend.types.apifox import ApifoxModel
from src.common.database.service import Service
from src.core.datacls import ApifoxDataclass


class HomeService:
    def __init__(self):
        self._service = Service()

    def get_mmd_count(self) -> int:
        return self._service.get_mmd_count()

    def get_tag_count(self) -> int:
        return self._service.get_tag_count()

    def get_mmd(self, query: ApifoxModel):
        api_dataclass = ApifoxDataclass(
                limit=query.limit,
                offset=query.offset,
                author=query.author,
                download_status=query.download_status.value if query.download_status else None,
                mmd_id=query.mmd_id,
                post_time_search_begin=query.post_time_search_begin,
                post_time_search_end=query.post_time_search_end,
                rating=query.rating,
                score=query.score,
                score_operation=query.score_operation,
                sort_by=query.sort_by,
                status=query.status.value if query.status else None,
                tag_operation=query.tag_operation,
                tags=query.tags
                )
        return self._service.get_mmd(api_dataclass)

    def get_all_tag(self):
        return self._service.get_tag()
