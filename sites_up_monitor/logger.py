from typing import *

from .network import Site


class Logger:
    def __init__(self, output_loc):
        self.output_loc = output_loc
        self.output_format = '{} | {} | {} | {:.2f}ms | {}'

    def log(self, site: Site):
        with open(self.output_loc, 'a') as file:
            self._log_site(site, file)

    def _log_site(self, site: Site, file):
        print(site, file=file)
        for ping_result in site.ping_results:
            if ping_result.port != '???':
                port = f'{ping_result.port} | '
                if ping_result.port_status: port += 'open'
                else: port += 'unknown'
            else:
                port = ping_result.port
            print(
                self.output_format.format(
                    ping_result.time,
                    site.host_name,
                    ping_result.address,
                    ping_result.rtt,
                    port
                ),
                file=file
            )
        print('\n', file=file)
