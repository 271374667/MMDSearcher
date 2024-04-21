from typing import Dict, List

import loguru
from feapder.pipelines import BasePipeline

from src.common.crawler.items import MMDItem
from src.common.database.curd import Curd
from src.core.datacls import TagData
from datetime import datetime


class Pipeline(BasePipeline):
    """
    pipeline 是单线程的，批量保存数据的操作，不建议在这里写网络请求代码，如下载图片等
    """

    def __init__(self):
        self._curd = Curd()
        self._count: int = 0

    def save_items(self, table, items: List[Dict]) -> bool:
        """
        保存数据
        Args:
            table: 表名
            items: 数据，[{},{},...]

        Returns: 是否保存成功 True / False
                 若False，不会将本批数据入到去重库，以便再次入库

        """
        self._count += 1
        for item in items:
            if isinstance(item, MMDItem):
                tags = item.tags.split("#")
                tags_data = [TagData(tag_en_name=tag, tag_cn_name="", create_time=datetime.now()) for tag in tags]
                mmd_data = item.to_dict()
                tag_data = mmd_data.pop("tag")
                self._curd.add(mmd_data, tag_data)
        loguru.logger.debug(f'成功将第{self._count}批数据保存到数据库, 共{len(items)}条')
        return True
