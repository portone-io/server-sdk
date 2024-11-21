from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_fee_input import PlatformFeeInput, _deserialize_platform_fee_input, _serialize_platform_fee_input
from ...platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer

@dataclass
class CreatePlatformAdditionalFeePolicyBody:
    """추가 수수료 정책 생성을 위한 입력 정보
    """
    name: str
    """이름
    """
    fee: PlatformFeeInput
    """수수료 정보
    """
    vat_payer: PlatformPayer
    """부가세 부담 주체
    """
    id: Optional[str] = field(default=None)
    """생성할 추가 수수료 정책 아이디

    명시하지 않으면 id 가 임의로 생성됩니다.
    """
    memo: Optional[str] = field(default=None)
    """메모
    """


def _serialize_create_platform_additional_fee_policy_body(obj: CreatePlatformAdditionalFeePolicyBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["name"] = obj.name
    entity["fee"] = _serialize_platform_fee_input(obj.fee)
    entity["vatPayer"] = _serialize_platform_payer(obj.vat_payer)
    if obj.id is not None:
        entity["id"] = obj.id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_create_platform_additional_fee_policy_body(obj: Any) -> CreatePlatformAdditionalFeePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "fee" not in obj:
        raise KeyError(f"'fee' is not in {obj}")
    fee = obj["fee"]
    fee = _deserialize_platform_fee_input(fee)
    if "vatPayer" not in obj:
        raise KeyError(f"'vatPayer' is not in {obj}")
    vat_payer = obj["vatPayer"]
    vat_payer = _deserialize_platform_payer(vat_payer)
    if "id" in obj:
        id = obj["id"]
        if not isinstance(id, str):
            raise ValueError(f"{repr(id)} is not str")
    else:
        id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return CreatePlatformAdditionalFeePolicyBody(name, fee, vat_payer, id, memo)
