from datetime import datetime
from typing import Optional

from feapder import Item


class MMDItem(Item):
    __unique_key__ = ["url"]

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.mmd_id: Optional[int] = None
        self.post_time: Optional[datetime] = None
        self.author: Optional[str] = None
        self.pic_size: Optional[str] = None
        self.pic_url: Optional[str] = None
        self.source: Optional[str] = None
        self.rating: Optional[str] = None
        self.score: Optional[int] = None
        self.tags: Optional[str] = None
        self.url: Optional[str] = None
        self.create_time: Optional[datetime] = None
        self.update_time: Optional[datetime] = None
        self.status: Optional[int] = None
        self.download_status: Optional[int] = None
        self.tag_en_name: Optional[str] = None
        self.tag_cn_name: Optional[str] = None
        self.tag_create_time: Optional[datetime] = None
