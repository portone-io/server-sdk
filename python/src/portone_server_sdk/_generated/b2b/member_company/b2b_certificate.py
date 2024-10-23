from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.member_company.b2b_certificate_type import B2bCertificateType, _deserialize_b2b_certificate_type, _serialize_b2b_certificate_type

@dataclass
class B2bCertificate:
    registered_at: str
    """등록일시
    (RFC 3339 date-time)
    """
    expired_at: str
    """만료일시
    (RFC 3339 date-time)
    """
    issuer_name: str
    """발행자명
    """
    subject_name: str
    """본인명
    """
    certificate_type: B2bCertificateType
    """인증서 타입
    """
    oid: str
    """OID
    """
    registrant_contact_name: str
    """등록 담당자 성명
    """
    registrant_contact_id: str
    """등록 담당자 ID
    """


def _serialize_b2b_certificate(obj: B2bCertificate) -> Any:
    entity = {}
    entity["registeredAt"] = obj.registered_at
    entity["expiredAt"] = obj.expired_at
    entity["issuerName"] = obj.issuer_name
    entity["subjectName"] = obj.subject_name
    entity["certificateType"] = _serialize_b2b_certificate_type(obj.certificate_type)
    entity["oid"] = obj.oid
    entity["registrantContactName"] = obj.registrant_contact_name
    entity["registrantContactId"] = obj.registrant_contact_id
    return entity


def _deserialize_b2b_certificate(obj: Any) -> B2bCertificate:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "registeredAt" not in obj:
        raise KeyError(f"'registeredAt' is not in {obj}")
    registered_at = obj["registeredAt"]
    if not isinstance(registered_at, str):
        raise ValueError(f"{repr(registered_at)} is not str")
    if "expiredAt" not in obj:
        raise KeyError(f"'expiredAt' is not in {obj}")
    expired_at = obj["expiredAt"]
    if not isinstance(expired_at, str):
        raise ValueError(f"{repr(expired_at)} is not str")
    if "issuerName" not in obj:
        raise KeyError(f"'issuerName' is not in {obj}")
    issuer_name = obj["issuerName"]
    if not isinstance(issuer_name, str):
        raise ValueError(f"{repr(issuer_name)} is not str")
    if "subjectName" not in obj:
        raise KeyError(f"'subjectName' is not in {obj}")
    subject_name = obj["subjectName"]
    if not isinstance(subject_name, str):
        raise ValueError(f"{repr(subject_name)} is not str")
    if "certificateType" not in obj:
        raise KeyError(f"'certificateType' is not in {obj}")
    certificate_type = obj["certificateType"]
    certificate_type = _deserialize_b2b_certificate_type(certificate_type)
    if "oid" not in obj:
        raise KeyError(f"'oid' is not in {obj}")
    oid = obj["oid"]
    if not isinstance(oid, str):
        raise ValueError(f"{repr(oid)} is not str")
    if "registrantContactName" not in obj:
        raise KeyError(f"'registrantContactName' is not in {obj}")
    registrant_contact_name = obj["registrantContactName"]
    if not isinstance(registrant_contact_name, str):
        raise ValueError(f"{repr(registrant_contact_name)} is not str")
    if "registrantContactId" not in obj:
        raise KeyError(f"'registrantContactId' is not in {obj}")
    registrant_contact_id = obj["registrantContactId"]
    if not isinstance(registrant_contact_id, str):
        raise ValueError(f"{repr(registrant_contact_id)} is not str")
    return B2bCertificate(registered_at, expired_at, issuer_name, subject_name, certificate_type, oid, registrant_contact_name, registrant_contact_id)
