import socket
from collections import namedtuple
from contextlib import closing
from typing import List, Tuple


class Site:

    def __init__(self, host_name, ports=''):
        self.host_name = host_name
        self.ports = []
        self._check_ports(ports)
        self._fetch_ips()
    
    def _check_ports(self, ports):
        for port in ports.split(','):
            self._check_single_port(port)
    
    def _check_single_port(self, port):
        if port.isnumeric():
            try:
                self.ports.append(
                    (
                        port,
                        self._is_port_open(int(port))
                    )
                )
            except:
                print('Warning: Something wrong with network')

    def _is_port_open(self, port):
        with closing(
            socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        ) as sock:
            sock.settimeout(3)
            return sock.connect_ex((self.host_name, port)) == 0

    def _fetch_ips(self):
        if not self.host_name:
            self.host_name = '???'
        elif self.host_name[0].isdigit():
            self.addresses = [self.host_name]
            self.host_name = '???'
            return
        try:
            self.addresses = socket.gethostbyname_ex(self.host_name)[2]
        except:
            self.addresses = []
        # Remove duplicate addresses
        self.addresses = {*self.addresses}

    def __str__(self):
        string_representation = f'''[\'{self.host_name}\', {list(self.addresses)}, {list(port[0] for port in self.ports)}]'''
        if hasattr(self, 'cert_valid'):
            print(f'has attr cert valid {self.host_name}')
            string_representation += ' valid cert' if self.cert_valid else 'INVALID cert'
        return f'''[\'{self.host_name}\', {list(self.addresses)}, {list(port[0] for port in self.ports)}]'''
