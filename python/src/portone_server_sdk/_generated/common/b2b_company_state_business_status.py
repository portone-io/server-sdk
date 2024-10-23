from __future__ import annotations
from typing import Any, Literal, Optional

B2bCompanyStateBusinessStatus = Literal["IN_BUSINESS", "CLOSED", "SUSPENDED"]
"""영업 상태
"""


def _serialize_b2b_company_state_business_status(obj: B2bCompanyStateBusinessStatus) -> Any:
    return obj


def _deserialize_b2b_company_state_business_status(obj: Any) -> B2bCompanyStateBusinessStatus:
    if obj not in ["IN_BUSINESS", "CLOSED", "SUSPENDED"]:
        raise ValueError(f"{repr(obj)} is not B2bCompanyStateBusinessStatus")
    return obj
