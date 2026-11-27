from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...common.selected_channel import SelectedChannel, _deserialize_selected_channel, _serialize_selected_channel

@dataclass
class CancelledCashReceipt:
    """발급 취소
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
    """승인번호
    """
    issued_at: str
    """발급 시점
    (RFC 3339 date-time)
    """
    cancelled_at: str
    """취소 시점
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
    status_updated_at: Optional[str] = field(default=None)
    """상태 업데이트 시점
    (RFC 3339 date-time)
    """


def _serialize_cancelled_cash_receipt(obj: CancelledCashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = "CANCELLED"
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
    entity["cancelledAt"] = obj.cancelled_at
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
    if obj.status_updated_at is not None:
        entity["statusUpdatedAt"] = obj.status_updated_at
    return entity


def _deserialize_cancelled_cash_receipt(obj: Any) -> CancelledCashReceipt:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    if status != "CANCELLED":
        raise ValueError("Expected 'CANCELLED' for status")
    if "merchantId" not in obj:
        raise KeyError("Missing required field 'merchantId'")
    merchant_id = obj["merchantId"]
    if not isinstance(merchant_id, str):
        raise ValueError("Expected str for merchant_id")
    if "storeId" not in obj:
        raise KeyError("Missing required field 'storeId'")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError("Expected str for store_id")
    if "paymentId" not in obj:
        raise KeyError("Missing required field 'paymentId'")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError("Expected str for payment_id")
    if "channel" not in obj:
        raise KeyError("Missing required field 'channel'")
    channel = obj["channel"]
    channel = _deserialize_selected_channel(channel)
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    if "currency" not in obj:
        raise KeyError("Missing required field 'currency'")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    if "orderName" not in obj:
        raise KeyError("Missing required field 'orderName'")
    order_name = obj["orderName"]
    if not isinstance(order_name, str):
        raise ValueError("Expected str for order_name")
    if "isManual" not in obj:
        raise KeyError("Missing required field 'isManual'")
    is_manual = obj["isManual"]
    if not isinstance(is_manual, bool):
        raise ValueError("Expected bool for is_manual")
    if "issueNumber" not in obj:
        raise KeyError("Missing required field 'issueNumber'")
    issue_number = obj["issueNumber"]
    if not isinstance(issue_number, str):
        raise ValueError("Expected str for issue_number")
    if "issuedAt" not in obj:
        raise KeyError("Missing required field 'issuedAt'")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError("Expected str for issued_at")
    if "cancelledAt" not in obj:
        raise KeyError("Missing required field 'cancelledAt'")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError("Expected str for cancelled_at")
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
    if "type" in obj:
        type = obj["type"]
        type = _deserialize_cash_receipt_type(type)
    else:
        type = None
    if "pgReceiptId" in obj:
        pg_receipt_id = obj["pgReceiptId"]
        if not isinstance(pg_receipt_id, str):
            raise ValueError("Expected str for pg_receipt_id")
    else:
        pg_receipt_id = None
    if "url" in obj:
        url = obj["url"]
        if not isinstance(url, str):
            raise ValueError("Expected str for url")
    else:
        url = None
    if "statusUpdatedAt" in obj:
        status_updated_at = obj["statusUpdatedAt"]
        if not isinstance(status_updated_at, str):
            raise ValueError("Expected str for status_updated_at")
    else:
        status_updated_at = None
    return CancelledCashReceipt(merchant_id, store_id, payment_id, channel, amount, currency, order_name, is_manual, issue_number, issued_at, cancelled_at, tax_free_amount, vat_amount, type, pg_receipt_id, url, status_updated_at)
