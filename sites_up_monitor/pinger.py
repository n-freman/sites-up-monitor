import abc
from datetime import datetime
from statistics import mean

from pythonping import ping
from tcping import Ping
from tcp_latency import measure_latency

from .network import Site


class IPinger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ping(self, ping: Site):
        raise NotImplementedError


class ICMPPinger(IPinger):
    def __init__(self, site: Site):
        self.site = site
        self.addresses = site.addresses

    def ping(self):
        self.site.ping_results = []
        for address in self.site.addresses:
            self._ping_single(address)
    
    def _ping_single(self, address):
        result = ping(address)
        self.site.ping_results.append(
            PingResult(
                address,
                result.rtt_avg_ms
            )
        )


class TCPPingerV1(IPinger):
    def __init__(self, site: Site):
        self.site = site

    def ping(self):
        # self.results = tcp_ping(address, port)
        self.site.ping_results = []
        for address in self.site.addresses:
            for port in self.site.ports:
                self._ping_single(address, port)
    
    def _ping_single(self, address, port):
        ping_obj = Ping(address, port[0])
        try:
            ping_obj.ping()
            rtt = mean(ping_obj._conn_times) # Average round trip time
        except:
            rtt = 2000
        self.site.ping_results.append(
            PingResult(
                address,
                # Average round trip time
                rtt,
                port
            )
        )


class TCPPingerV2(IPinger):
    def __init__(self, site: Site):
        self.site = site

    def ping(self):
        for address in self.site.addresses:
            for port in self.site.ports:
                self._ping_single(address, port)
    
    def _ping_single(self, address, port):
        if port[1]:
            ping_output = measure_latency(address, port)
            rtt = mean(ping_output)
            self.site.ping_results.append(
                PingResult(
                    address,
                    rtt,
                    port
                )
            )


class PingerFactory:
    @staticmethod
    def build_pinger(site: Site):
        if site.ports:
            return TCPPingerV1(site)
        else:
            return ICMPPinger(site)


class PingResult:
    def __init__(self, address, rtt, port=None):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%-M:%-S.%f')
        self.address = address
        self.rtt = rtt
        self.port = port[0] if port else '???'
        if self.port != '???':
            self.port_status = port[1]

    def __str__(self):
        return f'''
        {self.time}
        {self.address}
        {self.rtt}
        {self.port}
        '''
