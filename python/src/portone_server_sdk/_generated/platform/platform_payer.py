from __future__ import annotations
from typing import Any, Literal, Optional

PlatformPayer = Literal["PARTNER", "MERCHANT"]
"""금액 부담 주체

플랫폼에서 발생한 결제 수수료, 부가세 등 금액을 부담하는 주체를 나타냅니다.
"""


def _serialize_platform_payer(obj: PlatformPayer) -> Any:
    return obj


def _deserialize_platform_payer(obj: Any) -> PlatformPayer:
    if obj not in ["PARTNER", "MERCHANT"]:
        raise ValueError(f"{repr(obj)} is not PlatformPayer")
    return obj
