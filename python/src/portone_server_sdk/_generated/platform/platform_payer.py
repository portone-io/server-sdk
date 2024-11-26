from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformPayer = Union[Literal["PARTNER", "MERCHANT"], str]
"""금액 부담 주체

플랫폼에서 발생한 결제 수수료, 부가세 등 금액을 부담하는 주체를 나타냅니다.
"""


def _serialize_platform_payer(obj: PlatformPayer) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_payer(obj: Any) -> PlatformPayer:
    return obj
