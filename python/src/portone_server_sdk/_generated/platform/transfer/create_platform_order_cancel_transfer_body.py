from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.create_platform_order_cancel_transfer_body_discount import CreatePlatformOrderCancelTransferBodyDiscount, _deserialize_create_platform_order_cancel_transfer_body_discount, _serialize_create_platform_order_cancel_transfer_body_discount
from portone_server_sdk._generated.platform.transfer.create_platform_order_cancel_transfer_body_external_cancellation_detail import CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, _deserialize_create_platform_order_cancel_transfer_body_external_cancellation_detail, _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail
from portone_server_sdk._generated.platform.transfer.create_platform_order_cancel_transfer_body_order_detail import CreatePlatformOrderCancelTransferBodyOrderDetail, _deserialize_create_platform_order_cancel_transfer_body_order_detail, _serialize_create_platform_order_cancel_transfer_body_order_detail
from portone_server_sdk._generated.platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value

@dataclass
class CreatePlatformOrderCancelTransferBody:
    """주문 취소 정산 등록을 위한 입력 정보

    하나의 payment에 하나의 정산 건만 존재하는 경우에는 (partnerId, paymentId)로 취소 정산을 등록하실 수 있습니다.
    하나의 payment에 여러 개의 정산 건이 존재하는 경우에는 transferId를 필수로 입력해야 합니다.
    transferId를 입력한 경우 (partnerId, paymentId)는 생략 가능합니다.
    """
    cancellation_id: str
    """취소 내역 아이디
    """
    discounts: list[CreatePlatformOrderCancelTransferBodyDiscount]
    """할인 정보
    """
    partner_id: Optional[str]
    """파트너 아이디
    """
    payment_id: Optional[str]
    """결제 아이디
    """
    transfer_id: Optional[str]
    """정산건 아이디
    """
    memo: Optional[str]
    """메모
    """
    order_detail: Optional[CreatePlatformOrderCancelTransferBodyOrderDetail]
    """주문 취소 정보
    """
    tax_free_amount: Optional[int]
    """주문 취소 면세 금액

    주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
    (int64)
    """
    settlement_start_date: Optional[str]
    """정산 시작일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    external_cancellation_detail: Optional[CreatePlatformOrderCancelTransferBodyExternalCancellationDetail]
    """외부 결제 상세 정보

    해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
    """
    is_for_test: Optional[bool]
    """테스트 모드 여부

    기본값은 false 입니다.
    """
    user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]]
    """사용자 정의 속성
    """


def _serialize_create_platform_order_cancel_transfer_body(obj: CreatePlatformOrderCancelTransferBody) -> Any:
    entity = {}
    entity["cancellationId"] = obj.cancellation_id
    entity["discounts"] = list(map(_serialize_create_platform_order_cancel_transfer_body_discount, obj.discounts))
    if obj.partner_id is not None:
        entity["partnerId"] = obj.partner_id
    if obj.payment_id is not None:
        entity["paymentId"] = obj.payment_id
    if obj.transfer_id is not None:
        entity["transferId"] = obj.transfer_id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.order_detail is not None:
        entity["orderDetail"] = _serialize_create_platform_order_cancel_transfer_body_order_detail(obj.order_detail)
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.settlement_start_date is not None:
        entity["settlementStartDate"] = obj.settlement_start_date
    if obj.external_cancellation_detail is not None:
        entity["externalCancellationDetail"] = _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(obj.external_cancellation_detail)
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    return entity


def _deserialize_create_platform_order_cancel_transfer_body(obj: Any) -> CreatePlatformOrderCancelTransferBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cancellationId" not in obj:
        raise KeyError(f"'cancellationId' is not in {obj}")
    cancellation_id = obj["cancellationId"]
    if not isinstance(cancellation_id, str):
        raise ValueError(f"{repr(cancellation_id)} is not str")
    if "discounts" not in obj:
        raise KeyError(f"'discounts' is not in {obj}")
    discounts = obj["discounts"]
    if not isinstance(discounts, list):
        raise ValueError(f"{repr(discounts)} is not list")
    for i, item in enumerate(discounts):
        item = _deserialize_create_platform_order_cancel_transfer_body_discount(item)
        discounts[i] = item
    if "partnerId" in obj:
        partner_id = obj["partnerId"]
        if not isinstance(partner_id, str):
            raise ValueError(f"{repr(partner_id)} is not str")
    else:
        partner_id = None
    if "paymentId" in obj:
        payment_id = obj["paymentId"]
        if not isinstance(payment_id, str):
            raise ValueError(f"{repr(payment_id)} is not str")
    else:
        payment_id = None
    if "transferId" in obj:
        transfer_id = obj["transferId"]
        if not isinstance(transfer_id, str):
            raise ValueError(f"{repr(transfer_id)} is not str")
    else:
        transfer_id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "orderDetail" in obj:
        order_detail = obj["orderDetail"]
        order_detail = _deserialize_create_platform_order_cancel_transfer_body_order_detail(order_detail)
    else:
        order_detail = None
    if "taxFreeAmount" in obj:
        tax_free_amount = obj["taxFreeAmount"]
        if not isinstance(tax_free_amount, int):
            raise ValueError(f"{repr(tax_free_amount)} is not int")
    else:
        tax_free_amount = None
    if "settlementStartDate" in obj:
        settlement_start_date = obj["settlementStartDate"]
        if not isinstance(settlement_start_date, str):
            raise ValueError(f"{repr(settlement_start_date)} is not str")
    else:
        settlement_start_date = None
    if "externalCancellationDetail" in obj:
        external_cancellation_detail = obj["externalCancellationDetail"]
        external_cancellation_detail = _deserialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(external_cancellation_detail)
    else:
        external_cancellation_detail = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        if not isinstance(user_defined_properties, list):
            raise ValueError(f"{repr(user_defined_properties)} is not list")
        for i, item in enumerate(user_defined_properties):
            item = _deserialize_platform_user_defined_property_key_value(item)
            user_defined_properties[i] = item
    else:
        user_defined_properties = None
    return CreatePlatformOrderCancelTransferBody(cancellation_id, discounts, partner_id, payment_id, transfer_id, memo, order_detail, tax_free_amount, settlement_start_date, external_cancellation_detail, is_for_test, user_defined_properties)
