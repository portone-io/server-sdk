from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class IssuedCashReceipt:
    """발급 완료
    """
    """현금영수증 상태
    """
    merchant_id: str
    """고객사 아이디
    """
    store_id: str
    """상점 아이디
    """
    payment_id: str
    """결제 건 아이디
    """
    channel: SelectedChannel
    """현금영수증 발급에 사용된 채널
    """
    amount: int
    """결제 금액
    (int64)
    """
    currency: Currency
    """통화
    """
    order_name: str
    """주문명
    """
    is_manual: bool
    """수동 발급 여부
    """
    issue_number: str
    """승인 번호
    """
    issued_at: str
    """발급 시점
    (RFC 3339 date-time)
    """
    tax_free_amount: Optional[int] = field(default=None)
    """면세액
    (int64)
    """
    vat_amount: Optional[int] = field(default=None)
    """부가세액
    (int64)
    """
    type: Optional[CashReceiptType] = field(default=None)
    """현금영수증 유형
    """
    pg_receipt_id: Optional[str] = field(default=None)
    """PG사 현금영수증 아이디
    """
    url: Optional[str] = field(default=None)
    """현금영수증 URL
    """


def _serialize_issued_cash_receipt(obj: IssuedCashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "ISSUED"
    entity["merchantId"] = obj.merchant_id
    entity["storeId"] = obj.store_id
    entity["paymentId"] = obj.payment_id
    entity["channel"] = _serialize_selected_channel(obj.channel)
    entity["amount"] = obj.amount
    entity["currency"] = _serialize_currency(obj.currency)
    entity["orderName"] = obj.order_name
    entity["isManual"] = obj.is_manual
    entity["issueNumber"] = obj.issue_number
    entity["issuedAt"] = obj.issued_at
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.vat_amount is not None:
        entity["vatAmount"] = obj.vat_amount
    if obj.type is not None:
        entity["type"] = _serialize_cash_receipt_type(obj.type)
    if obj.pg_receipt_id is not None:
        entity["pgReceiptId"] = obj.pg_receipt_id
    if obj.url is not None:
        entity["url"] = obj.url
    return entity


def _deserialize_issued_cash_receipt(obj: Any) -> IssuedCashReceipt:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "ISSUED":
        raise ValueError(f"{repr(status)} is not 'ISSUED'")
    if "merchantId" not in obj:
        raise KeyError(f"'merchantId' is not in {obj}")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError(f"{repr(merchant_id)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "channel" not in obj:
        raise KeyError(f"'channel' is not in {obj}")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "orderName" not in obj:
        raise KeyError(f"'orderName' is not in {obj}")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError(f"{repr(order_name)} is not str")
    if "isManual" not in obj:
        raise KeyError(f"'isManual' is not in {obj}")
    is_manual = obj["isManual"]
    if not isinstance(is_manual, bool):
        raise ValueError(f"{repr(is_manual)} is not bool")
    if "issueNumber" not in obj:
        raise KeyError(f"'issueNumber' is not in {obj}")
    issue_number = obj["issueNumber"]
    if not isinstance(issue_number, str):
        raise ValueError(f"{repr(issue_number)} is not str")
    if "issuedAt" not in obj:
        raise KeyError(f"'issuedAt' is not in {obj}")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError(f"{repr(issued_at)} is not str")
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "vatAmount" in obj:
        vat_amount = obj["vatAmount"]
        if not isinstance(vat_amount, int):
            raise ValueError(f"{repr(vat_amount)} is not int")
    else:
        vat_amount = None
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_cash_receipt_type(type)
    else:
        type = None
    if "pgReceiptId" in obj:
        pg_receipt_id = obj["pgReceiptId"]
        if not isinstance(pg_receipt_id, str):
            raise ValueError(f"{repr(pg_receipt_id)} is not str")
    else:
        pg_receipt_id = None
    if "url" in obj:
        url = obj["url"]
        if not isinstance(url, str):
            raise ValueError(f"{repr(url)} is not str")
    else:
        url = None
    return IssuedCashReceipt(merchant_id, store_id, payment_id, channel, amount, currency, order_name, is_manual, issue_number, issued_at, tax_free_amount, vat_amount, type, pg_receipt_id, url)
