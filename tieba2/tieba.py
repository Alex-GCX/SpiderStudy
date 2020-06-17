import requests
from lxml import etree


class TiebaSpider:
    def __init__(self, name):
        self.name = name
        self.start_url = "https://tieba.baidu.com/f?kw={}".format(name)
        self.host = "https://tieba.baidu.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
        self.page_num = 1

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.content.decode().replace('-->', '').replace('<!--', ''))
        return html

    def parse_list(self, list_html):
        # 解析列表页, 获取每个帖子的url
        detail_url_list = list_html.xpath("//li[@class=' j_thread_list clearfix']//a[@class='j_th_tit ']/@href")
        # 循环发送帖子详情页请求并解析
        for detail_url in detail_url_list:
            self.parse_detail(detail_url)
        # 循环请求下一页
        next_page_url = list_html.xpath("//a[contains(text(),'下一页')]/@href")
        if next_page_url:
            # 拼接完整下一页url
            next_page_url = 'https:' + next_page_url[0]
        return next_page_url

    def parse_detail(self, detail_url):
        # 初始化
        detail_img_list = []
        next_page_url = detail_url
        title = None
        while next_page_url:
            # 拼接详情完整url
            detail_url = self.host + next_page_url
            print(detail_url)
            # 发送帖子详情请求,获取详情页响应
            detail_html = self.parse_url(detail_url)
            # 获取帖子标题
            if not title:
                title = detail_html.xpath("//h1[@class='core_title_txt  ']/@title")[0]
            print('第{}页: 标题:{}'.format(self.page_num, title))
            # 获取图片
            img_list = detail_html.xpath(
                "//div[contains(@class,'d_post_content j_d_post_content')]/img[@class='BDE_Image']/@src")
            print(img_list)
            if img_list:
                detail_img_list += img_list
            # 获取下一页
            next_page_url = detail_html.xpath("//a[text()='下一页']/@href")
            if next_page_url:
                next_page_url = next_page_url[0]
        if detail_img_list:
            # 保存该帖子的图片
            with open('tieba.txt', 'a', encoding='utf-8') as f:
                f.write('第{}页: 标题:{}\n'.format(self.page_num, title))
                for detail_img in detail_img_list:
                    f.write('{}\n'.format(detail_img))

    def main(self):
        # 获取url
        next_page_url = self.start_url
        while next_page_url:
            # 发送每一页请求,获取列表页响应
            list_html = self.parse_url(next_page_url)
            # 解析列表页面,获取详情页url和下一页url
            next_page_url = self.parse_list(list_html)
            self.page_num += 1
# //li[@class='j_thread_list clearfix']//a[@class='j_th_tit']/@href
#//div[contains(@class,"d_post_content j_d_post_content")]/img[@class='BDE_Image']/@src


if __name__ == '__main__':
    tieba_spider = TiebaSpider('汉得')
    tieba_spider.main()
