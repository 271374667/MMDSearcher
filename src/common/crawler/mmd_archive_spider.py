import feapder


class MMDArchiveSpider(feapder.AirSpider):
    __custom_setting__ = dict(
        REQUEST_FILTER_ENABLE=True,  # request 去重
        # REQUEST_FILTER_SETTING=dict(
        #     filter_type=3,  # 永久去重（BloomFilter） = 1 、内存去重（MemoryFilter） = 2、 临时去重（ExpireFilter）= 3、 轻量去重（LiteFilter）= 4
        #     expire_time=2592000,  # 过期时间1个月
        # ),
        REQUEST_FILTER_SETTING=dict(
            filter_type=4,  # 永久去重（BloomFilter） = 1 、内存去重（MemoryFilter） = 2、 临时去重（ExpireFilter）= 3、 轻量去重（LiteFilter）= 4
        ),
    )

    def start_requests(self):
        yield feapder.Request("https://mmda.booru.org/index.php?page=post&s=list")

    def parse(self, request: feapder.Request, response: feapder.Response):
        # 获取下一页的链接
        next_page = response.xpath('//div[@id="paginator"]/a/@href')[-1].extract()


if __name__ == "__main__":
    MMDArchiveSpider().start()