import ssl
from datetime import datetime

import OpenSSL

from .network import Site


class CertChecker:

    def check_certificate(self, site: Site):
        for port in site.ports:
            if self._port_could_have_cert(port):
                self._check_cert(
                    site.host_name,
                    port
                )
                break

    @staticmethod
    def _port_could_have_cert(port):
        return port[1] and str(port[0]) == '443'
    
    @staticmethod
    def _check_cert(domain, port):
        try:
            site.cert_exists = False
            certificate = ssl.get_server_certificate(
                (domain, port)
            )
        except:
            pass
        else:
            site.cert_exists = True
            site.cert_valid = self._is_certificate_valid(
                certificate
            )

    @staticmethod
    def _is_certificate_valid(certificate):
        expiration_time = self._get_certificate_expiration_time(
            certificate
        )
        return expiration_time > datetime.now()

    @staticmethod
    def _get_certificate_expiration_time(certificate):
        x509 = OpenSSL.crypto.load_certificate(
            OpenSSL.crypto.FILETYPE_PEM,
            certificate
        )
        bytes=x509.get_notAfter()
        timestamp = bytes.decode('utf-8')
        expiration_time = datetime.strptime(
            timestamp,
            '%Y%m%d%H%M%S%z'
        ).date()
        return expiration_time
