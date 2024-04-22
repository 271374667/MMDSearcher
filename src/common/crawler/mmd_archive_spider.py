from datetime import datetime
from typing import Optional

import feapder
import loguru

from src.common.crawler.baidu_translate import BaiduTranslate
from src.common.crawler.items import MMDItem
from src.core.datacls import TagData
from src.common.database.curd import Curd


class MMDArchiveSpider(feapder.AirSpider):
    __custom_setting__ = dict(
            REQUEST_FILTER_ENABLE=True,  # request 去重
            REQUEST_FILTER_SETTING=dict(
                    filter_type=4,
                    # 永久去重（BloomFilter） = 1 、内存去重（MemoryFilter） = 2、 临时去重（ExpireFilter）= 3、 轻量去重（LiteFilter）= 4
                    ),
            ITEM_PIPELINES={
                    'src.common.crawler.pipelines.Pipeline': 300,
                    }
            )

    def __init__(self, thread_count: Optional[int] = None):
        super().__init__(thread_count=thread_count)
        self._baidu_translate = BaiduTranslate()
        self._curd = Curd()

    def start_requests(self):
        yield feapder.Request("https://mmda.booru.org/index.php?page=post&s=list")

    def parse(self, request: feapder.Request, response: feapder.Response):
        # 获取本页所有的详情页
        detail_urls = response.xpath('//div[@class="content"]//span/a[not(@style)]/@href')  # 获取所有没有被隐藏的链接
        loguru.logger.debug(f"本页共有{len(detail_urls)}个详情页")
        for detail_url in detail_urls.extract():
            yield feapder.Request(detail_url, callback=self.parse_detail)

        # 获取下一页的链接
        next_page = response.xpath('//div[@id="paginator"]/a[contains(@alt, "next")]/@href')

        if next_page:
            yield feapder.Request(next_page.extract_first(), callback=self.parse)

    def parse_detail(self, request: feapder.Request, response: feapder.Response):
        item = MMDItem()
        # 获取所有的标签
        tag_list: list[str] = response.xpath('//div[@id="tag_list"]/ul/li/span/a/text()').extract()
        tags: str = "#".join(tag_list)
        item.tags = tags
        # 将标签里面的每一个值翻译成中文
        tag_data_list: list[TagData] = []
        for each in tag_list:
            tag_cn = self._baidu_translate.en2cn(each)
            loguru.logger.debug(f"{each} -> {tag_cn}")

            # 组装TagData
            tag_data = TagData(tag_en_name=each, tag_cn_name=tag_cn, create_time=datetime.now())
            tag_data_list.append(tag_data)

        (mmd_id, post_time, author, pic_size, source, rating, score) = response.xpath(
                '//div[@id="tag_list"]/ul/text()').extract()
        loguru.logger.debug(f'{mmd_id=} {post_time=} {author=} {pic_size=} {source=} {rating=} {score=}')
        item.mmd_id = int(mmd_id.split(":")[-1].strip())
        item.post_time = datetime.strptime(post_time.split(":", maxsplit=1)[-1].strip(), "%Y-%m-%d %H:%M:%S")
        item.author = author.split(":")[-1].strip()
        item.pic_size = pic_size.split(":")[-1].strip()
        item.pic_url = response.xpath('//div[@id="note-container"]/img/@src').extract_first()
        item.source = source.split(":")[-1].strip()
        item.rating = rating.split(":")[-1].strip()
        item.score = int(score.split(":")[-1].strip())
        item.tag_list = tag_data_list
        item.url = response.url
        item.create_time = datetime.now()
        item.update_time = datetime.now()
        item.status = 0
        item.download_status = 0

        if self._curd.get_mmd_query().filter_by(mmd_id=item.mmd_id).first():
            loguru.logger.debug(f"已经更新到最新版本, mmd_id={item.mmd_id}, 不再继续爬取")
            self.stop_spider()
        yield item


if __name__ == "__main__":
    MMDArchiveSpider(thread_count=2).start()
