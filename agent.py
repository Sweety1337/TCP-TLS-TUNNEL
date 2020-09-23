from python_socks.sync import Proxy
import clients
import socket


class TunnelHttpAgent:
    """
    This class used to tunnel or create
    a socket that is connected
    to our proxy server
    """
    def __init__(self, host=None, server_name=None, server_port=None, port=None, auth=None, proxy=None, client=None, timeout=None):
        """
        TIMEOUT: 5
        DEFAULT CLIENT: CHROME
        CLIENTS: CHROME, IOS, FIREFOX
        """
        self.host = host
        self.port = port
        self.auth = auth
        self.proxy = proxy
        self.client = client
        self.timeout = timeout
        self.server_name = server_name
        self.server_port = server_port
        self.tunnel_proxy = f'http://{self.auth["login"]}:{self.auth["password"]}@{self.host}:{self.port}'

        if self.server_name is None:
            raise AttributeError('Invalid server name')

        if self.auth is None:
            raise AttributeError('Invalid proxy authentication data')

        if self.server_port is None:
            self.server_port = 443

        if self.timeout is None:
            self.timeout = 5

        if self.client is None:
            self.client = clients.Clients.CHROME.value

        if self.proxy is None:
            self.proxy = ''

        self.tunneling()

    def tunneling(self):
        """
        This is the main
        function that parses
        the proxy and
        creates a tunnel.
        """

        self.socket_connection = Proxy.from_url(
            url=self.tunnel_proxy,
            client=clients.Clients[self.client.upper()].value,
            proxy=self.proxy
        )

        self.sock = self.socket_connection.connect(
            dest_host=self.server_name,
            dest_port=self.server_port,
            timeout=self.timeout,
        )

    def close(self):
        self.sock.close()


"""
This is an example 
of using the class

tunnelHttpAgent = TunnelHttpAgent(
    host='127.0.0.1',
    port=443,
    server_name='www.howsmyssl.com',
    server_port=443,
    auth={
        'login': 'test1',
        'password': 'test2'
    },
    proxy='https://login:password@ip:port',
    client='CHROME',
    timeout=5
)
"""
