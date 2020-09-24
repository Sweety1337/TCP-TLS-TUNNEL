from http.client import HTTPConnection
from urllib.parse import urlparse
import urllib3
import sys

sys.path.append('src')

from agent import TunnelHttpAgent


auth = {
    'login': 'TEST-LOGIN',
    'password': 'TEST-PASSWORD'
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
        host='127.0.0.1',
        port=8080,
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
    url = 'https://www.howsmyssl.com/a/check'
    method = 'GET'
    r = request(
        url=url,
        method=method,
        timeout=5,
        proxy='',
        client='CHROME'
    )
    data = r.getresponse().read().decode('utf-8')
    print(data)
