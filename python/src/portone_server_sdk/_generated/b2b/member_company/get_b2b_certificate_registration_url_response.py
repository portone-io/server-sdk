from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class GetB2bCertificateRegistrationUrlResponse:
    """인증서 등록 URL 조회 응답 정보
    """
    url: str
    """인증서 등록 URL
    """


def _serialize_get_b2b_certificate_registration_url_response(obj: GetB2bCertificateRegistrationUrlResponse) -> Any:
    entity = {}
    entity["url"] = obj.url
    return entity


def _deserialize_get_b2b_certificate_registration_url_response(obj: Any) -> GetB2bCertificateRegistrationUrlResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "url" not in obj:
        raise KeyError(f"'url' is not in {obj}")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError(f"{repr(url)} is not str")
    return GetB2bCertificateRegistrationUrlResponse(url)
