from __future__ import annotations
from typing import Any, Literal, Optional

B2bCompanyStateTaxationType = Literal["NORMAL", "TAX_FREE", "SIMPLE", "SIMPLE_TAX_INVOICE_ISSUER", "ASSIGNED_ID_NUMBER"]
"""사업자 과세 유형
"""


def _serialize_b2b_company_state_taxation_type(obj: B2bCompanyStateTaxationType) -> Any:
    return obj


def _deserialize_b2b_company_state_taxation_type(obj: Any) -> B2bCompanyStateTaxationType:
    if obj not in ["NORMAL", "TAX_FREE", "SIMPLE", "SIMPLE_TAX_INVOICE_ISSUER", "ASSIGNED_ID_NUMBER"]:
        raise ValueError(f"{repr(obj)} is not B2bCompanyStateTaxationType")
    return obj
