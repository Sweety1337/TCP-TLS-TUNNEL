# TCP-TLS-TUNNEL

Provides Python Http and Https agents that establish TCP and TLS connections via our modified poxy server. Our TLS Layer pass ciphers and has SSL session ticket support by default. If you are really interested in testing it for free, you can find out more details in our Discord Channel.

Discord Channel: [TCP TLS Tunnel](https://discord.gg/4HRVxNP)

# Requirements

Install python-socks from [Here](https://github.com/Sweety1337/python-socks-upgraded) 
```
And put in site-packages like 
\Python\Python38-32\Lib\site-packages\python_socks
```


# Usage examples
Import [http.client](https://docs.python.org/3/library/http.client.html) [urllib3](https://urllib3.readthedocs.io/en/latest/) [sys](https://docs.python.org/3/library/sys.html) [urllib](https://docs.python.org/3/library/sys.html) [agent](https://github.com/Sweety1337/py-http-tunnel/src/agent.py)

```
from http.client import HTTPConnection
from urllib.parse import urlparse
import urllib3
import sys

sys.path.append('src')

from agent import TunnelHttpAgent
```

Firstly we have to create https Agent for https request:
```
tunnelHttpAgent = TunnelHttpAgent(
  host='HOST',
  port=443,
  server_name=host,
  server_port=port,
  auth=auth,
  timeout=timeout,
  proxy=proxy,
  client='CHROME',
)
```

Declare Auth and headers variables for the following request:
```
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
```

Example usage
```
def request(url: str, method: str = 'GET', timeout: int = 5, proxy: str = '', client: str = 'Chrome'):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    host = parsed_url.netloc
    if scheme == 'http':
        port = 80
    else:
        port = 443

    tunnelHttpAgent = TunnelHttpAgent(
        host='HOST',
        port=443,
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
    connection.sock = tunnelHttpAgent
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
        timeout=5
    )
    data = r.getresponse().read().decode('utf-8')
    print(data)
```
