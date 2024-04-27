"""
该模块主要用于浏览器传入之后的参数校验,后期在整个程序中的交互还是使用dataclass
"""
from typing import Optional

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from src.core.config import DEFAULT_PAGE_SIZE
from src.core.enums import DownloadStatus, Status


class ApifoxModel(BaseModel):
    limit: Optional[int] = DEFAULT_PAGE_SIZE
    offset: Optional[int] = 0
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
        if not self.limit or self.limit < 0:
            self.limit = DEFAULT_PAGE_SIZE
        if not self.offset or self.offset < 0:
            self.offset = 0
        return self

    @model_validator(mode='after')
    def check_enums(self):
        if self.download_status and not DownloadStatus.has_value(self.download_status):
            raise ValueError(f"download_status must be one of {DownloadStatus.values()}")
        if self.status and not Status.has_value(self.status):
            raise ValueError(f"status must be one of {Status.values()}")
        return self


if __name__ == '__main__':
    # model = ApifoxModel(
    #         limit=10,
    #         offset=0,
    #         author="test",
    #         download_status=DownloadStatus.UNKNOWN_WEBSITE,
    #         mmd_id=1,
    #         post_time_search_begin="2022-01-01",
    #         post_time_search_end="2022-12-31",
    #         rating="safe",
    #         score=100,
    #         score_operation=2,
    #         sort_by="post_time",
    #         status=1,
    #         tag_operation=1,
    #         tags="tag1#tag2#tag3"
    #         )
    model = ApifoxModel(limit=10, offset=0)
    print(model)
    # print(model)
    # print(model.json())
