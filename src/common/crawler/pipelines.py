from typing import Dict, List

import loguru
from feapder.pipelines import BasePipeline

from src.common.crawler.items import MMDItem
from src.common.database.curd import Curd


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
                self._curd.add(
                        mmd_id=item.mmd_id,
                        post_time=item.post_time,
                        author=item.author,
                        pic_size=item.pic_size,
                        pic_url=item.pic_url,
                        source=item.source,
                        rating=item.rating,
                        score=item.score,
                        tags=item.tags,
                        url=item.url,
                        create_time=item.create_time,
                        update_time=item.update_time,
                        status=item.status,
                        download_status=item.download_status,
                        tag_en_name=item.tag_en_name,
                        tag_cn_name=item.tag_cn_name,
                        tag_create_time=item.tag_create_time
                        )
        loguru.logger.debug(f'成功将第{self._count}批数据保存到数据库, 共{len(items)}条')
        return True
