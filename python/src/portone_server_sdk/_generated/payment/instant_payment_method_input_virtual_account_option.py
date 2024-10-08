from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account_option_fixed import InstantPaymentMethodInputVirtualAccountOptionFixed, _deserialize_instant_payment_method_input_virtual_account_option_fixed, _serialize_instant_payment_method_input_virtual_account_option_fixed
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account_option_type import InstantPaymentMethodInputVirtualAccountOptionType, _deserialize_instant_payment_method_input_virtual_account_option_type, _serialize_instant_payment_method_input_virtual_account_option_type

@dataclass
class InstantPaymentMethodInputVirtualAccountOption:
    """가상계좌 발급 방식
    """
    type: InstantPaymentMethodInputVirtualAccountOptionType
    """발급 유형
    """
    fixed: Optional[InstantPaymentMethodInputVirtualAccountOptionFixed]
    """고정식 가상계좌 발급 방식

    발급 유형을 FIXED 로 선택했을 시에만 입력합니다.
    """


def _serialize_instant_payment_method_input_virtual_account_option(obj: InstantPaymentMethodInputVirtualAccountOption) -> Any:
    entity = {}
    entity["type"] = _serialize_instant_payment_method_input_virtual_account_option_type(obj.type)
    if obj.fixed is not None:
        entity["fixed"] = _serialize_instant_payment_method_input_virtual_account_option_fixed(obj.fixed)
    return entity


def _deserialize_instant_payment_method_input_virtual_account_option(obj: Any) -> InstantPaymentMethodInputVirtualAccountOption:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    type = _deserialize_instant_payment_method_input_virtual_account_option_type(type)
    if "fixed" in obj:
        fixed = obj["fixed"]
        fixed = _deserialize_instant_payment_method_input_virtual_account_option_fixed(fixed)
    else:
        fixed = None
    return InstantPaymentMethodInputVirtualAccountOption(type, fixed)
