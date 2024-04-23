from typing import Dict, List

import loguru
from feapder.pipelines import BasePipeline

from src.common.database.curd import Curd
from src.core.datacls import MMDData


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
        print(items)
        self._count += 1
        for item in items:
            mmd_data = MMDData(
                    mmd_id=item.get('mmd_id'),
                    post_time=item.get('post_time'),
                    author=item.get('author'),
                    pic_size=item.get('pic_size'),
                    pic_url=item.get('pic_url'),
                    source=item.get('source'),
                    rating=item.get('rating'),
                    score=item.get('score'),
                    tags=item.get('tags'),
                    url=item.get('url'),
                    create_time=item.get('create_time'),
                    update_time=item.get('update_time'),
                    status=item.get('status'),
                    download_status=item.get('download_status')
                    )
            self._curd.add(mmd_data, item.get('tag_list'))
            loguru.logger.debug(f'成功保存一条数据到数据库, mmd_id={item.get("mmd_id")}')

        # loguru.logger.debug(f'成功将第{self._count}批数据保存到数据库, 共{len(items)}条')
        return True
