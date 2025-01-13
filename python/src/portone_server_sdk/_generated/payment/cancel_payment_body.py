from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.cancel_payment_body_refund_account import CancelPaymentBodyRefundAccount, _deserialize_cancel_payment_body_refund_account, _serialize_cancel_payment_body_refund_account
from ..payment.cancel_requester import CancelRequester, _deserialize_cancel_requester, _serialize_cancel_requester
from ..payment.promotion_discount_retain_option import PromotionDiscountRetainOption, _deserialize_promotion_discount_retain_option, _serialize_promotion_discount_retain_option

@dataclass
class CancelPaymentBody:
    """결제 취소 요청 입력 정보
    """
    reason: str
    """취소 사유
    """
    store_id: Optional[str] = field(default=None)
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    amount: Optional[int] = field(default=None)
    """취소 총 금액

    값을 입력하지 않으면 전액 취소됩니다.
    (int64)
    """
    tax_free_amount: Optional[int] = field(default=None)
    """취소 금액 중 면세 금액

    값을 입력하지 않으면 전액 과세 취소됩니다.
    (int64)
    """
    vat_amount: Optional[int] = field(default=None)
    """취소 금액 중 부가세액

    값을 입력하지 않으면 자동 계산됩니다.
    (int64)
    """
    requester: Optional[CancelRequester] = field(default=None)
    """취소 요청자

    고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
    """
    promotion_discount_retain_option: Optional[PromotionDiscountRetainOption] = field(default=None)
    """프로모션 할인율 유지 옵션

    프로모션이 적용된 결제를 부분 취소하는 경우, 최초 할인율을 유지할지 여부를 선택할 수 있습니다.
    RETAIN 으로 설정 시, 최초 할인율을 유지할 수 있도록 취소 금액이 조정됩니다.
    RELEASE 으로 설정 시, 취소 후 남은 금액이 속한 구간에 맞게 프로모션 할인이 새롭게 적용됩니다.
    값을 입력하지 않으면 RELEASE 로 취급합니다.
    """
    current_cancellable_amount: Optional[int] = field(default=None)
    """결제 건의 취소 가능 잔액

    본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
    (int64)
    """
    refund_account: Optional[CancelPaymentBodyRefundAccount] = field(default=None)
    """환불 계좌

    계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
    """


def _serialize_cancel_payment_body(obj: CancelPaymentBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["reason"] = obj.reason
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.amount is not None:
        entity["amount"] = obj.amount
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.vat_amount is not None:
        entity["vatAmount"] = obj.vat_amount
    if obj.requester is not None:
        entity["requester"] = _serialize_cancel_requester(obj.requester)
    if obj.promotion_discount_retain_option is not None:
        entity["promotionDiscountRetainOption"] = _serialize_promotion_discount_retain_option(obj.promotion_discount_retain_option)
    if obj.current_cancellable_amount is not None:
        entity["currentCancellableAmount"] = obj.current_cancellable_amount
    if obj.refund_account is not None:
        entity["refundAccount"] = _serialize_cancel_payment_body_refund_account(obj.refund_account)
    return entity


def _deserialize_cancel_payment_body(obj: Any) -> CancelPaymentBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "reason" not in obj:
        raise KeyError(f"'reason' is not in {obj}")
    reason = obj["reason"]
    if not isinstance(reason, str):
        raise ValueError(f"{repr(reason)} is not str")
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "amount" in obj:
        amount = obj["amount"]
        if not isinstance(amount, int):
            raise ValueError(f"{repr(amount)} is not int")
    else:
        amount = None
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
    if "requester" in obj:
        requester = obj["requester"]
        requester = _deserialize_cancel_requester(requester)
    else:
        requester = None
    if "promotionDiscountRetainOption" in obj:
        promotion_discount_retain_option = obj["promotionDiscountRetainOption"]
        promotion_discount_retain_option = _deserialize_promotion_discount_retain_option(promotion_discount_retain_option)
    else:
        promotion_discount_retain_option = None
    if "currentCancellableAmount" in obj:
        current_cancellable_amount = obj["currentCancellableAmount"]
        if not isinstance(current_cancellable_amount, int):
            raise ValueError(f"{repr(current_cancellable_amount)} is not int")
    else:
        current_cancellable_amount = None
    if "refundAccount" in obj:
        refund_account = obj["refundAccount"]
        refund_account = _deserialize_cancel_payment_body_refund_account(refund_account)
    else:
        refund_account = None
    return CancelPaymentBody(reason, store_id, amount, tax_free_amount, vat_amount, requester, promotion_discount_retain_option, current_cancellable_amount, refund_account)
