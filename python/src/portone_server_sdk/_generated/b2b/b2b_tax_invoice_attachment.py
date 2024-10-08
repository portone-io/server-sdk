from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bTaxInvoiceAttachment:
    """세금계산서 첨부파일
    """
    id: str
    """첨부 파일 아이디
    """
    name: str
    """첨부 파일명
    """
    attached_at: str
    """첨부 일시
    (RFC 3339 date-time)
    """


def _serialize_b2b_tax_invoice_attachment(obj: B2bTaxInvoiceAttachment) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["name"] = obj.name
    entity["attachedAt"] = obj.attached_at
    return entity


def _deserialize_b2b_tax_invoice_attachment(obj: Any) -> B2bTaxInvoiceAttachment:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "attachedAt" not in obj:
        raise KeyError(f"'attachedAt' is not in {obj}")
    attached_at = obj["attachedAt"]
    if not isinstance(attached_at, str):
        raise ValueError(f"{repr(attached_at)} is not str")
    return B2bTaxInvoiceAttachment(id, name, attached_at)
