from urllib.parse import quote


def encode_path_parameter(value: str) -> str:
    encoded = quote(value, safe="")
    if encoded == "":
        raise ValueError("Path parameters cannot be empty.")
    if encoded in (".", ".."):
        raise ValueError("Path parameters cannot be dot segments.")
    return encoded
