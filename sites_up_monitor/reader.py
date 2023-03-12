import csv
from typing import Iterable, Tuple


class Reader:
    def __init__(self, path: str) -> None:
        self.path = path
 
    def read(self):
        result = []
        with open(self.path) as data_file:
            data_reader = csv.reader(data_file, delimiter=';')
            for row in data_reader:
                result.append(row)
        return result[1:]
