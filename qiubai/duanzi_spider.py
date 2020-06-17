import requests
import re
from pprint import pprint


class DuanziSpider:
    def __init__(self):
        self.temp_url = 'https://www.qiushibaike.com/text/page/{}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36User-Agent",
            #"Referer": "https://www.qiushibaike.com/",
        }

    # def main(self):
    #     page = 1
    #     has_next = True
    #     while has_next:
    #         # 构造网址
    #         url = self.temp_url.format(page)
    #         print(url)
    #         # 发送请求,获取响应
    #         response = requests.get(url, headers=self.headers)
    #         # 提取html信息
    #         html = response.content.decode()
    #         # 提取段子信息
    #         item_list = re.findall(r'<div class="content">\s<span>(.*?)</span>', html, re.S)
    #         # 提取下一页
    #         has_next = re.match(r'.*?<span class="next">', html, re.S)
    #         # 保存段子
    #         with open('duanzi.html', 'a', encoding='utf-8') as f:
    #             for item in item_list:
    #                 text = item.strip().replace('<br/><br/>', '<br/>').replace('<br/>', '\n')
    #                 f.write('第{}页,第{}条:\n{}\n\n'.format(page, item_list.index(item) + 1, text))
    #         # 循环下一页
    #         page += 1
    def main(self):
        next_page = 1
        while next_page:
            # 构造网址
            url = self.temp_url.format(next_page)
            print(url)
            # 发送请求,获取响应
            response = requests.get(url, headers=self.headers)
            # 提取html信息
            html = response.content.decode()
            # 提取段子信息
            item_list = re.findall(r'<div class="content">\s<span>(.*?)</span>', html, re.S)
            # 保存段子
            with open('duanzi.html', 'a', encoding='utf-8') as f:
                for item in item_list:
                    text = item.strip().replace('<br/><br/>', '<br/>').replace('<br/>', '\n')
                    f.write('第{}页,第{}条:\n{}\n\n'.format(next_page, item_list.index(item) + 1, text))
            # 提取下一页url
            next_page = re.findall(
                r'<!--<a href="/text/page/(\d*)/" rel="nofollow">-->\s<span class="next">', html, re.S)
            if next_page:
                next_page = next_page[0]


if __name__ == '__main__':
    duanzi_spider = DuanziSpider()
    duanzi_spider.main()
