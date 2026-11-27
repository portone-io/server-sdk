import re
from urllib.parse import quote


def encode_path_parameter(value: str) -> str:
    encoded = quote(value, safe="")
    # A literal dot stays ".", while a caller-supplied "%2e" becomes "%252e".
    if re.fullmatch(r"(?:\.|%252[eE]){1,2}", encoded):
        raise ValueError("Path parameters cannot be dot segments.")
    return encoded
