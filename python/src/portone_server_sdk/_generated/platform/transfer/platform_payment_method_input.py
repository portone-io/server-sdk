from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_payment_method_card_input import PlatformPaymentMethodCardInput, _deserialize_platform_payment_method_card_input, _serialize_platform_payment_method_card_input
from ...platform.transfer.platform_payment_method_easy_pay_input import PlatformPaymentMethodEasyPayInput, _deserialize_platform_payment_method_easy_pay_input, _serialize_platform_payment_method_easy_pay_input
from ...platform.transfer.platform_payment_method_gift_certificate_input import PlatformPaymentMethodGiftCertificateInput, _deserialize_platform_payment_method_gift_certificate_input, _serialize_platform_payment_method_gift_certificate_input
from ...platform.transfer.platform_payment_method_mobile_input import PlatformPaymentMethodMobileInput, _deserialize_platform_payment_method_mobile_input, _serialize_platform_payment_method_mobile_input
from ...platform.transfer.platform_payment_method_transfer_input import PlatformPaymentMethodTransferInput, _deserialize_platform_payment_method_transfer_input, _serialize_platform_payment_method_transfer_input
from ...platform.transfer.platform_payment_method_virtual_account_input import PlatformPaymentMethodVirtualAccountInput, _deserialize_platform_payment_method_virtual_account_input, _serialize_platform_payment_method_virtual_account_input

@dataclass
class PlatformPaymentMethodInput:
    """결제 수단 입력 정보
    """
    card: Optional[PlatformPaymentMethodCardInput] = field(default=None)
    """카드
    """
    transfer: Optional[PlatformPaymentMethodTransferInput] = field(default=None)
    """계좌이체
    """
    virtual_account: Optional[PlatformPaymentMethodVirtualAccountInput] = field(default=None)
    """가상계좌
    """
    gift_certificate: Optional[PlatformPaymentMethodGiftCertificateInput] = field(default=None)
    """상품권
    """
    mobile: Optional[PlatformPaymentMethodMobileInput] = field(default=None)
    """모바일
    """
    easy_pay: Optional[PlatformPaymentMethodEasyPayInput] = field(default=None)
    """간편 결제
    """


def _serialize_platform_payment_method_input(obj: PlatformPaymentMethodInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.card is not None:
        entity["card"] = _serialize_platform_payment_method_card_input(obj.card)
    if obj.transfer is not None:
        entity["transfer"] = _serialize_platform_payment_method_transfer_input(obj.transfer)
    if obj.virtual_account is not None:
        entity["virtualAccount"] = _serialize_platform_payment_method_virtual_account_input(obj.virtual_account)
    if obj.gift_certificate is not None:
        entity["giftCertificate"] = _serialize_platform_payment_method_gift_certificate_input(obj.gift_certificate)
    if obj.mobile is not None:
        entity["mobile"] = _serialize_platform_payment_method_mobile_input(obj.mobile)
    if obj.easy_pay is not None:
        entity["easyPay"] = _serialize_platform_payment_method_easy_pay_input(obj.easy_pay)
    return entity


def _deserialize_platform_payment_method_input(obj: Any) -> PlatformPaymentMethodInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_platform_payment_method_card_input(card)
    else:
        card = None
    if "transfer" in obj:
        transfer = obj["transfer"]
        transfer = _deserialize_platform_payment_method_transfer_input(transfer)
    else:
        transfer = None
    if "virtualAccount" in obj:
        virtual_account = obj["virtualAccount"]
        virtual_account = _deserialize_platform_payment_method_virtual_account_input(virtual_account)
    else:
        virtual_account = None
    if "giftCertificate" in obj:
        gift_certificate = obj["giftCertificate"]
        gift_certificate = _deserialize_platform_payment_method_gift_certificate_input(gift_certificate)
    else:
        gift_certificate = None
    if "mobile" in obj:
        mobile = obj["mobile"]
        mobile = _deserialize_platform_payment_method_mobile_input(mobile)
    else:
        mobile = None
    if "easyPay" in obj:
        easy_pay = obj["easyPay"]
        easy_pay = _deserialize_platform_payment_method_easy_pay_input(easy_pay)
    else:
        easy_pay = None
    return PlatformPaymentMethodInput(card, transfer, virtual_account, gift_certificate, mobile, easy_pay)
