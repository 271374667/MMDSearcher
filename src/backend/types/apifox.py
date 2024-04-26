from typing import Optional

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from src.core.enums import DownloadStatus, Status


class ApifoxModel(BaseModel):
    limit: int
    offset: int
    author: Optional[str] = None
    download_status: Optional[DownloadStatus] = None
    mmd_id: Optional[int] = None
    post_time_search_begin: Optional[str] = None
    post_time_search_end: Optional[str] = None
    rating: Optional[str] = None
    score: Optional[int] = None
    score_operation: Optional[int] = None
    sort_by: Optional[str] = None
    status: Optional[Status] = None
    tag_operation: Optional[int] = None
    tags: Optional[str] = None

    @model_validator(mode='after')
    def check_positive(self) -> Self:
        if self.limit < 0 or self.offset < 0:
            raise ValueError("limit and offset must be a positive number")
        return self

    @model_validator(mode='after')
    def check_not_empty(self):
        if self.author is None or not self.author.strip():
            raise ValueError("author must not be an empty string")
        if self.post_time_search_begin is None or not self.post_time_search_begin.strip():
            raise ValueError("post_time_search_begin must not be an empty string")
        if self.post_time_search_end is None or not self.post_time_search_end.strip():
            raise ValueError("post_time_search_end must not be an empty string")
        if self.rating is None or not self.rating.strip():
            raise ValueError("rating must not be an empty string")
        if self.sort_by is None or not self.sort_by.strip():
            raise ValueError("sort_by must not be an empty string")
        if self.tags is None or not self.tags.strip():
            raise ValueError("tags must not be an empty string")
        return self

    @model_validator(mode='after')
    def check_enums(self):
        if self.download_status and not DownloadStatus.has_value(self.download_status):
            raise ValueError(f"download_status must be one of {DownloadStatus.values()}")
        if self.status and not Status.has_value(self.status):
            raise ValueError(f"status must be one of {Status.values()}")
        return self


if __name__ == '__main__':
    model = ApifoxModel(
            limit=10,
            offset=0,
            author="test",
            download_status=DownloadStatus.UNKNOWN_WEBSITE,
            mmd_id=1,
            post_time_search_begin="2022-01-01",
            post_time_search_end="2022-12-31",
            rating="safe",
            score=100,
            score_operation=2,
            sort_by="post_time",
            status=1,
            tag_operation=1,
            tags="tag1#tag2#tag3"
            )
    print(model)
    print(model.json())
