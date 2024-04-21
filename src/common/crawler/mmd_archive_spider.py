import feapder
import loguru

from src.common.crawler.items import MMDItem


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

        item.mmd_id = int(response.url.split("=")[-1])
        item.post_time = response.xpath('//div[@id="stats"]/ul/li[1]/text()').extract_first()
        item.author = response.xpath('//div[@id="stats"]/ul/li[2]/a/text()').extract_first()
        item.pic_size = response.xpath('//div[@id="stats"]/ul/li[3]/text()').extract_first()
        item.pic_url = response.xpath('//div[@id="image"]/a/img/@src').extract_first()
        item.source = response.xpath('//div[@id="image"]/a/@href').extract_first()
        item.rating = response.xpath('//div[@id="stats"]/ul/li[4]/text()').extract_first()
        item.score = int(response.xpath('//div[@id="stats"]/ul/li[5]/text()').extract_first())
        item.tags = response.xpath('//div[@id="tag-list"]/ul/li/a/text()').extract()
        item.url = response.url
        yield item


if __name__ == "__main__":
    MMDArchiveSpider().start()
