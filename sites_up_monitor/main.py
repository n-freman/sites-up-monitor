import logger
import reader
import config as conf


class App():
    def __init__(self):
        self.reader = reader.Reader(conf.INPUT_DATA)
        self.logger = logger.Logger()

    def run(self):
        ...


app = App()

if __name__ == '__main__':
    app.run()
