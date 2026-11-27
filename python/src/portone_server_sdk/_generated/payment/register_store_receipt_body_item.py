from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class RegisterStoreReceiptBodyItem:
    """하위 상점 거래 정보
    """
    store_business_registration_number: str
    """하위 상점 사업자등록번호
    """
    store_name: str
    """하위 상점명
    """
    total_amount: int
    """결제 총 금액
    (int64)
    """
    currency: Currency
    """통화
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세액
    (int64)
    """
    vat_amount: Optional[int] = field(default=None)
    """부가세액
    (int64)
    """
    supply_amount: Optional[int] = field(default=None)
    """공급가액
    (int64)
    """


def _serialize_register_store_receipt_body_item(obj: RegisterStoreReceiptBodyItem) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["storeBusinessRegistrationNumber"] = obj.store_business_registration_number
    entity["storeName"] = obj.store_name
    entity["totalAmount"] = obj.total_amount
    entity["currency"] = _serialize_currency(obj.currency)
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.vat_amount is not None:
        entity["vatAmount"] = obj.vat_amount
    if obj.supply_amount is not None:
        entity["supplyAmount"] = obj.supply_amount
    return entity


def _deserialize_register_store_receipt_body_item(obj: Any) -> RegisterStoreReceiptBodyItem:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "storeBusinessRegistrationNumber" not in obj:
        raise KeyError("Missing required field 'storeBusinessRegistrationNumber'")
    store_business_registration_number = obj["storeBusinessRegistrationNumber"]
    if not isinstance(store_business_registration_number, str):
        raise ValueError("Expected str for store_business_registration_number")
    if "storeName" not in obj:
        raise KeyError("Missing required field 'storeName'")
    store_name = obj["storeName"]
    if not isinstance(store_name, str):
        raise ValueError("Expected str for store_name")
    if "totalAmount" not in obj:
        raise KeyError("Missing required field 'totalAmount'")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError("Expected int for total_amount")
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError("Expected int for tax_free_amount")
    else:
        tax_free_amount = None
    if "vatAmount" in obj:
        vat_amount = obj["vatAmount"]
        if not isinstance(vat_amount, int):
            raise ValueError("Expected int for vat_amount")
    else:
        vat_amount = None
    if "supplyAmount" in obj:
        supply_amount = obj["supplyAmount"]
        if not isinstance(supply_amount, int):
            raise ValueError("Expected int for supply_amount")
    else:
        supply_amount = None
    return RegisterStoreReceiptBodyItem(store_business_registration_number, store_name, total_amount, currency, tax_free_amount, vat_amount, supply_amount)
