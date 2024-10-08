from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_fee_input import PlatformFeeInput, _deserialize_platform_fee_input, _serialize_platform_fee_input
from portone_server_sdk._generated.platform.platform_payer import PlatformPayer, _deserialize_platform_payer, _serialize_platform_payer

@dataclass
class UpdatePlatformAdditionalFeePolicyBody:
    """추가 수수료 정책 업데이트를 위한 입력 정보

    값이 명시하지 않은 필드는 업데이트되지 않습니다.
    """
    fee: Optional[PlatformFeeInput]
    """책정 수수료
    """
    name: Optional[str]
    """추가 수수료 정책 이름
    """
    memo: Optional[str]
    """해당 추가 수수료 정책에 대한 메모
    """
    vat_payer: Optional[PlatformPayer]
    """부가세를 부담할 주체
    """


def _serialize_update_platform_additional_fee_policy_body(obj: UpdatePlatformAdditionalFeePolicyBody) -> Any:
    entity = {}
    if obj.fee is not None:
        entity["fee"] = _serialize_platform_fee_input(obj.fee)
    if obj.name is not None:
        entity["name"] = obj.name
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.vat_payer is not None:
        entity["vatPayer"] = _serialize_platform_payer(obj.vat_payer)
    return entity


def _deserialize_update_platform_additional_fee_policy_body(obj: Any) -> UpdatePlatformAdditionalFeePolicyBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "fee" in obj:
        fee = obj["fee"]
        fee = _deserialize_platform_fee_input(fee)
    else:
        fee = None
    if "name" in obj:
        name = obj["name"]
        if not isinstance(name, str):
            raise ValueError(f"{repr(name)} is not str")
    else:
        name = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "vatPayer" in obj:
        vat_payer = obj["vatPayer"]
        vat_payer = _deserialize_platform_payer(vat_payer)
    else:
        vat_payer = None
    return UpdatePlatformAdditionalFeePolicyBody(fee, name, memo, vat_payer)
