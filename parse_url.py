import requests
from retry import retry


@retry(tries=3)
def _parse_url(url, data=None):
    print('*' * 20)
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
    if data:
        response = requests.post(url, headers=headers, data=data)
    else:
        response = requests.get(url, headers=headers)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, data=None):
    try:
        return _parse_url(url, data)
    except Exception as e:
        return None


if __name__ == '__main__':
    print(parse_url('http://www.baidu.com'))
