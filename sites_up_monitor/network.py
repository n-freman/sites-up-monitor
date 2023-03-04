from collections import namedtuple

from pythonping import ping


Address = namedtuple('Address', ['ip', 'port'])


class Networker:
    def __init__(self):
        self._addresses: Address[str, int] = {}

    def fetch_ips(self, host_name):
        ...
    
    def ping(self):
        ...

