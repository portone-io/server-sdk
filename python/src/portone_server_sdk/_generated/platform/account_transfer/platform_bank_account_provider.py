from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBankAccountProvider = Union[Literal["HYPHEN_DATA", "HYPHEN_FIRM", "DOZN", "MOCK"], str]
"""제공자
"""


def _serialize_platform_bank_account_provider(obj: PlatformBankAccountProvider) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_bank_account_provider(obj: Any) -> PlatformBankAccountProvider:
    return obj
