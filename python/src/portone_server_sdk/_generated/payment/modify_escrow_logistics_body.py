from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_escrow_receiver_input import PaymentEscrowReceiverInput, _deserialize_payment_escrow_receiver_input, _serialize_payment_escrow_receiver_input
from portone_server_sdk._generated.payment.payment_escrow_sender_input import PaymentEscrowSenderInput, _deserialize_payment_escrow_sender_input, _serialize_payment_escrow_sender_input
from portone_server_sdk._generated.payment.payment_logistics import PaymentLogistics, _deserialize_payment_logistics, _serialize_payment_logistics
from portone_server_sdk._generated.common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product

@dataclass
class ModifyEscrowLogisticsBody:
    """에스크로 배송 정보 수정 입력 정보
    """
    logistics: PaymentLogistics
    """에스크로 물류 정보
    """
    store_id: Optional[str]
    """상점 아이디

    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    sender: Optional[PaymentEscrowSenderInput]
    """에스크로 발송자 정보
    """
    receiver: Optional[PaymentEscrowReceiverInput]
    """에스크로 수취인 정보
    """
    send_email: Optional[bool]
    """이메일 알림 전송 여부

    에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
    """
    products: Optional[list[PaymentProduct]]
    """상품 정보
    """


def _serialize_modify_escrow_logistics_body(obj: ModifyEscrowLogisticsBody) -> Any:
    entity = {}
    entity["logistics"] = _serialize_payment_logistics(obj.logistics)
    if obj.store_id is not None:
        entity["storeId"] = obj.store_id
    if obj.sender is not None:
        entity["sender"] = _serialize_payment_escrow_sender_input(obj.sender)
    if obj.receiver is not None:
        entity["receiver"] = _serialize_payment_escrow_receiver_input(obj.receiver)
    if obj.send_email is not None:
        entity["sendEmail"] = obj.send_email
    if obj.products is not None:
        entity["products"] = list(map(_serialize_payment_product, obj.products))
    return entity


def _deserialize_modify_escrow_logistics_body(obj: Any) -> ModifyEscrowLogisticsBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "logistics" not in obj:
        raise KeyError(f"'logistics' is not in {obj}")
    logistics = obj["logistics"]
    logistics = _deserialize_payment_logistics(logistics)
    if "storeId" in obj:
        store_id = obj["storeId"]
        if not isinstance(store_id, str):
            raise ValueError(f"{repr(store_id)} is not str")
    else:
        store_id = None
    if "sender" in obj:
        sender = obj["sender"]
        sender = _deserialize_payment_escrow_sender_input(sender)
    else:
        sender = None
    if "receiver" in obj:
        receiver = obj["receiver"]
        receiver = _deserialize_payment_escrow_receiver_input(receiver)
    else:
        receiver = None
    if "sendEmail" in obj:
        send_email = obj["sendEmail"]
        if not isinstance(send_email, bool):
            raise ValueError(f"{repr(send_email)} is not bool")
    else:
        send_email = None
    if "products" in obj:
        products = obj["products"]
        if not isinstance(products, list):
            raise ValueError(f"{repr(products)} is not list")
        for i, item in enumerate(products):
            item = _deserialize_payment_product(item)
            products[i] = item
    else:
        products = None
    return ModifyEscrowLogisticsBody(logistics, store_id, sender, receiver, send_email, products)
