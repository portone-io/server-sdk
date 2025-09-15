from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bBulkTaxInvoiceSourceType = Union[Literal["SHEET", "PLATFORM"], str]
"""그룹 생성 방식
"""


def _serialize_b2b_bulk_tax_invoice_source_type(obj: B2bBulkTaxInvoiceSourceType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_bulk_tax_invoice_source_type(obj: Any) -> B2bBulkTaxInvoiceSourceType:
    return obj
