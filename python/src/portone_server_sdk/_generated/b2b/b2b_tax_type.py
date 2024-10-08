from __future__ import annotations
from typing import Any, Literal, Optional

B2bTaxType = Literal["TAXABLE", "ZERO_RATED", "FREE"]
"""과세 유형
"""


def _serialize_b2b_tax_type(obj: B2bTaxType) -> Any:
    return obj


def _deserialize_b2b_tax_type(obj: Any) -> B2bTaxType:
    if obj not in ["TAXABLE", "ZERO_RATED", "FREE"]:
        raise ValueError(f"{repr(obj)} is not B2bTaxType")
    return obj
