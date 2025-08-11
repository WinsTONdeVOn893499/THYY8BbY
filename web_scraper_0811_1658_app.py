# 代码生成时间: 2025-08-11 16:58:25
import scrapy


# 定义一个Scrapy的Item，用于存储抓取的数据
class WebPageItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


# 定义一个Spider，用于抓取网页内容
class WebPageSpider(scrapy.Spider):
    name = "web_page_spider"
    allowed_domains = ["example.com"]  # 允许爬取的域名
    start_urls = [
        "http://example.com/page1",
        "http://example.com/page2"
    ]
# 优化算法效率

    def parse(self, response):
        # 提取网页标题
        title = response.css("title::text").get()

        # 提取网页内容
        content = response.css("div.content::text").getall()
        content = "
".join(content)

        # 创建一个Item对象
        item = WebPageItem()
        item["url"] = response.url
        item["title"] = title
        item["content"] = content

        # 将Item对象yield出去
        yield item

        # 提取下一页的链接并继续爬取
        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


# 主函数，用于启动Scrapy爬虫
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    # 创建一个CrawlerProcess对象
    process = CrawlerProcess()

    # 将Spider添加到CrawlerProcess中
# 改进用户体验
    process.crawl(WebPageSpider)

    # 启动爬虫
    process.start()
# FIXME: 处理边界情况