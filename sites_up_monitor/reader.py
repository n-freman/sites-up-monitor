import csv
from typing import Iterable


class Reader:
    def __init__(self, path: str) -> None:
        self.path = path
 
    def read(self) -> Iterable[Iterable[str, str]]:
        ...

