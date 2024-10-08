from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class PreRegisterPaymentBody:
    """결제 정보 사전 등록 입력 정보
    """
    store_id: Optional[str]
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    total_amount: Optional[int]
    """결제 총 금액
    (int64)
    """
    tax_free_amount: Optional[int]
    """결제 면세 금액
    (int64)
    """
    currency: Optional[Currency]
    """통화 단위
    """


def _serialize_pre_register_payment_body(obj: PreRegisterPaymentBody) -> Any:
    entity = {}
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.total_amount is not None:
        entity["totalAmount"] = obj.total_amount
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.currency is not None:
        entity["currency"] = _serialize_currency(obj.currency)
    return entity


def _deserialize_pre_register_payment_body(obj: Any) -> PreRegisterPaymentBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "totalAmount" in obj:
        total_amount = obj["totalAmount"]
        if not isinstance(total_amount, int):
            raise ValueError(f"{repr(total_amount)} is not int")
    else:
        total_amount = None
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "currency" in obj:
        currency = obj["currency"]
        currency = _deserialize_currency(currency)
    else:
        currency = None
    return PreRegisterPaymentBody(store_id, total_amount, tax_free_amount, currency)
