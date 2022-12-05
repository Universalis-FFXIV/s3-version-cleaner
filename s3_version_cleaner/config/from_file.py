from abc import ABC
import csv
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Credentials(ABC):
    user_name: str
    access_key_id: str
    secret_access_key: str


def parse_credentials_csv(iter: Iterable[str]):
    reader = csv.reader(iter)
    next(reader)  # Skip the header line
    [user_name, access_key_id, secret_access_key] = next(reader)
    return Credentials(user_name, access_key_id, secret_access_key)
