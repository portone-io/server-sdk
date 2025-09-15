from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bTaxInvoiceModificationType = Union[Literal["CORRECTION_OF_ENTRY_ERRORS", "CHANGE_IN_SUPPLY_COST", "RETURN", "CANCELLATION_OF_CONTRACT", "DUPLICATE_ISSUANCE_DUE_TO_ERROR"], str]
"""수정 사유
"""


def _serialize_b2b_tax_invoice_modification_type(obj: B2bTaxInvoiceModificationType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_tax_invoice_modification_type(obj: Any) -> B2bTaxInvoiceModificationType:
    return obj
