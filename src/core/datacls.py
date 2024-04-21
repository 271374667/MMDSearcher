from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class TagData:
    tag_en_name: str
    tag_cn_name: str
    create_time: datetime


@dataclass(slots=True, frozen=True)
class MMDData:
    mmd_id: int
    post_time: datetime
    author: str
    pic_size: str
    pic_url: str
    source: str
    rating: str
    score: int
    tags: str
    url: str
    create_time: datetime
    update_time: datetime
    status: int
    download_status: int
