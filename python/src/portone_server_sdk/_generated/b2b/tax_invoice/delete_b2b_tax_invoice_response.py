from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeleteB2bTaxInvoiceResponse:
    pass


def _serialize_delete_b2b_tax_invoice_response(obj: DeleteB2bTaxInvoiceResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    return entity


def _deserialize_delete_b2b_tax_invoice_response(obj: Any) -> DeleteB2bTaxInvoiceResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return DeleteB2bTaxInvoiceResponse()
