import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):     # 创建爬虫类, 必须继承scrapy.Spider类
    name = "dmoz"                    # 定义爬虫运行名字
    allowed_domains = ["dmoz.org"]       # 允许爬虫运行网站的列表(可选)
    start_urls = [
        "https://www.resource-zone.com/forum/f/general-dmoz-issues.4/"
    ]    # 定义爬虫启动入口

    def parse(self, response):                 # 定义爬虫传回参数, 用以处理
        for sel in response.xpath('//ul/li'):    # 提取数据, 查看网站列表所有元素
            item = DmozItem()                  # 使用Item
            # item['title'] = sel.xpath('a/text()').extract()  # Item提取网站标题
            item['link'] = sel.xpath('a/@href').extract()     # Item提取网站链接
            item['desc'] = sel.xpath('text()').extract()      # Item提取网站描述
            yield item    # yield返回item
        # 追踪链接,直到无法链接
        next_page = response.xpath('//li[@class="next"]/a/@href').extract()
        if next_page is not None:
            # yield返回请求
            yield scrapy.Request(response.urljoin(next_page))
