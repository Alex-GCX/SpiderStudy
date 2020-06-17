from pprint import pprint
import requests
import json
# url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=1592037988076"


class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18"
        self.headers = {
            "Referer": "https://m.douban.com/tv/american",
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"
        }

    def main(self):
        page = 0
        num = 1
        text = ''
        # 1.start_url
        while True:
            start_url = self.temp_url.format(page)
            # 2.发送请求,获取响应
            response = requests.get(start_url, headers=self.headers)
            # 3.解析数据
            dic = json.loads(response.content.decode())
            items = dic.get('subject_collection_items')
            # 3.提取数据
            for item in items:
                text = text + '第{}部:{},信息:{}\n'.format(str(num),
                                                       item['title'], item['info'])
                num += 1
            page += 18
            if page >= dic['total']:
                break
            # ret2 = json.dumps(dic, ensure_ascii=False, indent=4)
        with open("douban_tv.txt", "w", encoding="utf-8") as f:
            f.write(text)
            # pprint(ret2)
            # f.write(ret2)
        # 4.请求下一个url


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.main()
