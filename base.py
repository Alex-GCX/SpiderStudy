import requests
# 发送请求并获取响应
# response = requests.get('http://www.baidu.com')
# print('响应状态')
# print(response.status_code)
# # assert response.status_code == 300
# print('响应头')
# print(response.headers)
# print('响应内容')
# print(response.content.decode())
# print('请求头内容')
# print(response.request.headers)

# # 带headers的请求
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
# response = requests.get('http://www.baidu.com', headers=headers)
# print('响应内容')
# print(response.content.decode())

# 带参数的url请求
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
params = {'wd': 'python'}
response = requests.get(url=url, params=params, headers=headers)
# print('响应内容')
# print(response.content.decode())
print(response.request.url)
with open('baidu.html', 'wb') as f:
    f.write(response.content)
