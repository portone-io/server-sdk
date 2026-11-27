import re
from urllib.parse import quote


def encode_path_parameter(value: str) -> str:
    if re.fullmatch(r"(?:\.|%2[eE]){1,2}", value):
        raise ValueError("Path parameters cannot be dot segments.")
    return quote(value, safe="")
