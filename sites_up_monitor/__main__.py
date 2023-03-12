from . import config as conf
from .logger import Logger
from .reader import Reader
from .network import Site
from .pinger import PingerFactory


class App():
    def __init__(self):
        self.reader = Reader(conf.INPUT_DATA_FILE_LOC)
        self.logger = Logger(conf.OUPUT_DATA_FILE_LOC)
        self.sites = []
    
    def update(self):
        self.sites = []
        data = self.reader.read()
        for address in data:
            self.sites.append(Site(*address))
    
    def perform_checks(self):
        for site in self.sites:
            pinger = PingerFactory.build_pinger(site)
            pinger.ping()
            self.logger.log(site)

    def run(self):
        while True:
            self.update()
            self.perform_checks()


app = App()

if __name__ == '__main__':
    app.run()
