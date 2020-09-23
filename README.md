# TCP-TLS-TUNNEL

Provides Python Http and Https agents that establish TCP and TLS connections via our modified poxy server. Our TLS Layer pass ciphers and has SSL session ticket support by default. If you are really interested in testing it for free, you can find out more details in our Discord Channel.

Discord Channel: [TCP TLS Tunnel](https://discord.gg/4HRVxNP)

# Usage examples
Import [http.client](https://docs.python.org/3/library/http.client.html) [urllib3](https://urllib3.readthedocs.io/en/latest/) [sys](https://docs.python.org/3/library/sys.html) [urllib](https://docs.python.org/3/library/sys.html)

```
from http.client import HTTPConnection
from urllib.parse import urlparse
import urllib3
import sys
```
