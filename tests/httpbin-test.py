from http.client import HTTPConnection
from urllib.parse import urlparse
import urllib3
import sys

sys.path.append('src')

from agent import TunnelHttpAgent


auth = {
    'login': 'test1',
    'password': '467jw2d53x82FAGHSw'
}

headers = urllib3.make_headers(
    keep_alive=True,
    disable_cache=True,
    accept_encoding=True,
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
)


def request(url=None, method=None, timeout=None, proxy=None, client=None):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    host = parsed_url.netloc

    if scheme == 'http':
        port = 80
    else:
        port = 443

    tunnelHttpAgent = TunnelHttpAgent(
        host='104.248.43.30',
        port=1337,
        server_name=host,
        server_port=port,
        auth=auth,
        timeout=timeout,
        proxy=proxy,
        client=client,
    )

    connection = HTTPConnection(
        host=host,
        port=port,
        timeout=timeout
    )
    connection.sock = tunnelHttpAgent.sock
    connection.request(
        method=method,
        url=parsed_url.path,
        body=parsed_url.query,
        headers=headers
    )
    return connection


if __name__ == '__main__':
    url = 'https://www.httpbin.org/get'
    method = 'GET'
    r = request(
        url=url,
        method=method,
        timeout=5,
        proxy=None,
        client=None
    )
    data = r.getresponse().read().decode('utf-8')
    print(data)
