from __future__ import annotations
from typing import Any, Literal, Optional, Union

B2bCompanyStateBusinessStatus = Union[Literal["IN_BUSINESS", "CLOSED", "SUSPENDED"], str]
"""영업 상태
"""


def _serialize_b2b_company_state_business_status(obj: B2bCompanyStateBusinessStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_b2b_company_state_business_status(obj: Any) -> B2bCompanyStateBusinessStatus:
    return obj
