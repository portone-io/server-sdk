from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_certificate_type import B2bCertificateType, _deserialize_b2b_certificate_type, _serialize_b2b_certificate_type

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
    issuer_dn: str
    """발행자명
    """
    subject_dn: str
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
    entity["issuerDn"] = obj.issuer_dn
    entity["subjectDn"] = obj.subject_dn
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
    if "issuerDn" not in obj:
        raise KeyError(f"'issuerDn' is not in {obj}")
    issuer_dn = obj["issuerDn"]
    if not isinstance(issuer_dn, str):
        raise ValueError(f"{repr(issuer_dn)} is not str")
    if "subjectDn" not in obj:
        raise KeyError(f"'subjectDn' is not in {obj}")
    subject_dn = obj["subjectDn"]
    if not isinstance(subject_dn, str):
        raise ValueError(f"{repr(subject_dn)} is not str")
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
    return B2bCertificate(registered_at, expired_at, issuer_dn, subject_dn, certificate_type, oid, registrant_contact_name, registrant_contact_id)
