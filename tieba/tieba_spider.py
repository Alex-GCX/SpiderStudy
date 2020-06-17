import requests


# https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
tieba = input('请输入贴吧名\n')
base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(tieba)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
for page in range(5):
    url = base_url + str(page * 50)
    print(url)
    response = requests.get(url=url, headers=headers)
    with open(tieba + '_' + str(page) + '.html', 'w', encoding='utf-8') as f:
        f.write(response.content.decode())
