from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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


@dataclass(slots=True, frozen=True)
class ApifoxModel:
    """每一页最多读取多少个"""
    limit: int
    """偏移量"""
    offset: int
    """模型作者,可以模糊搜索"""
    author: Optional[str] = None
    """这一条记录的下载状态,0表示无法下载(比如链接失效,1表示可以下载,2代表未知网站"""
    download_status: Optional[int] = None
    """网站上的id"""
    mmd_id: Optional[int] = None
    """模型上传时间(起始搜索时间)"""
    post_time_search_begin: Optional[str] = None
    """模型上传时间(结束搜索时间)"""
    post_time_search_end: Optional[str] = None
    """模型的分级"""
    rating: Optional[str] = None
    """模型的评分"""
    score: Optional[int] = None
    """score搜索的运算符,0为等于,1为小于,2为大于"""
    score_operation: Optional[int] = None
    """这一条记录的状态,0表示还未看过,1表示已经看过"""
    status: Optional[int] = None
    """tag的搜索方式,0表示OR的关系,1表示AND的关系"""
    tag_operation: Optional[int] = None
    """模型的标签,用#分割,比如tag1#tag2#tag3"""
    tags: Optional[str] = None
