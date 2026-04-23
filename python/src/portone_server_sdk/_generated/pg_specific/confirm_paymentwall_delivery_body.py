from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.country import Country, _deserialize_country, _serialize_country
from ..pg_specific.paymentwall_delivery_status import PaymentwallDeliveryStatus, _deserialize_paymentwall_delivery_status, _serialize_paymentwall_delivery_status
from ..pg_specific.paymentwall_delivery_type import PaymentwallDeliveryType, _deserialize_paymentwall_delivery_type, _serialize_paymentwall_delivery_type

@dataclass
class ConfirmPaymentwallDeliveryBody:
    """페이먼트월 배송 정보 등록 입력 정보
    """
    transaction_id: str
    """결제 건 포트원 채번 아이디
    """
    delivery_type: PaymentwallDeliveryType
    """배송 유형
    """
    delivery_status: PaymentwallDeliveryStatus
    """배송 상태
    """
    estimated_delivery_datetime: str
    """배송 완료 예상 일시

    배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
    (RFC 3339 date-time)
    """
    estimated_update_datetime: str
    """배송 상태 업데이트 예정 일시

    배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
    (RFC 3339 date-time)
    """
    refundable: bool
    """환불 가능 여부
    """
    details: str
    """상세 설명
    """
    shipping_address_email: str
    """고객 이메일 주소
    """
    reason: Optional[str] = field(default=None)
    """상태 변경 사유
    """
    carrier_tracking_id: Optional[str] = field(default=None)
    """운송장 번호

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    carrier_type: Optional[str] = field(default=None)
    """운송사 이름

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_country: Optional[Country] = field(default=None)
    """수신자 국가

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_city: Optional[str] = field(default=None)
    """수신자 도시

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_zip: Optional[str] = field(default=None)
    """수신자 우편번호

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_state: Optional[str] = field(default=None)
    """수신자 주

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_street: Optional[str] = field(default=None)
    """수신자 도로명 주소

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_phone: Optional[str] = field(default=None)
    """수신자 전화번호

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_firstname: Optional[str] = field(default=None)
    """수신자 이름

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    shipping_address_lastname: Optional[str] = field(default=None)
    """수신자 성

    배송 유형이 PHYSICAL인 경우 필수입니다.
    """
    attachments: Optional[list[str]] = field(default=None)
    """배송 증빙 첨부 파일 URL 목록

    배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.
    """


def _serialize_confirm_paymentwall_delivery_body(obj: ConfirmPaymentwallDeliveryBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["transactionId"] = obj.transaction_id
    entity["deliveryType"] = _serialize_paymentwall_delivery_type(obj.delivery_type)
    entity["deliveryStatus"] = _serialize_paymentwall_delivery_status(obj.delivery_status)
    entity["estimatedDeliveryDatetime"] = obj.estimated_delivery_datetime
    entity["estimatedUpdateDatetime"] = obj.estimated_update_datetime
    entity["refundable"] = obj.refundable
    entity["details"] = obj.details
    entity["shippingAddressEmail"] = obj.shipping_address_email
    if obj.reason is not None:
        entity["reason"] = obj.reason
    if obj.carrier_tracking_id is not None:
        entity["carrierTrackingId"] = obj.carrier_tracking_id
    if obj.carrier_type is not None:
        entity["carrierType"] = obj.carrier_type
    if obj.shipping_address_country is not None:
        entity["shippingAddressCountry"] = _serialize_country(obj.shipping_address_country)
    if obj.shipping_address_city is not None:
        entity["shippingAddressCity"] = obj.shipping_address_city
    if obj.shipping_address_zip is not None:
        entity["shippingAddressZip"] = obj.shipping_address_zip
    if obj.shipping_address_state is not None:
        entity["shippingAddressState"] = obj.shipping_address_state
    if obj.shipping_address_street is not None:
        entity["shippingAddressStreet"] = obj.shipping_address_street
    if obj.shipping_address_phone is not None:
        entity["shippingAddressPhone"] = obj.shipping_address_phone
    if obj.shipping_address_firstname is not None:
        entity["shippingAddressFirstname"] = obj.shipping_address_firstname
    if obj.shipping_address_lastname is not None:
        entity["shippingAddressLastname"] = obj.shipping_address_lastname
    if obj.attachments is not None:
        entity["attachments"] = obj.attachments
    return entity


def _deserialize_confirm_paymentwall_delivery_body(obj: Any) -> ConfirmPaymentwallDeliveryBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "transactionId" not in obj:
        raise KeyError(f"'transactionId' is not in {obj}")
    transaction_id = obj["transactionId"]
    if not isinstance(transaction_id, str):
        raise ValueError(f"{repr(transaction_id)} is not str")
    if "deliveryType" not in obj:
        raise KeyError(f"'deliveryType' is not in {obj}")
    delivery_type = obj["deliveryType"]
    delivery_type = _deserialize_paymentwall_delivery_type(delivery_type)
    if "deliveryStatus" not in obj:
        raise KeyError(f"'deliveryStatus' is not in {obj}")
    delivery_status = obj["deliveryStatus"]
    delivery_status = _deserialize_paymentwall_delivery_status(delivery_status)
    if "estimatedDeliveryDatetime" not in obj:
        raise KeyError(f"'estimatedDeliveryDatetime' is not in {obj}")
    estimated_delivery_datetime = obj["estimatedDeliveryDatetime"]
    if not isinstance(estimated_delivery_datetime, str):
        raise ValueError(f"{repr(estimated_delivery_datetime)} is not str")
    if "estimatedUpdateDatetime" not in obj:
        raise KeyError(f"'estimatedUpdateDatetime' is not in {obj}")
    estimated_update_datetime = obj["estimatedUpdateDatetime"]
    if not isinstance(estimated_update_datetime, str):
        raise ValueError(f"{repr(estimated_update_datetime)} is not str")
    if "refundable" not in obj:
        raise KeyError(f"'refundable' is not in {obj}")
    refundable = obj["refundable"]
    if not isinstance(refundable, bool):
        raise ValueError(f"{repr(refundable)} is not bool")
    if "details" not in obj:
        raise KeyError(f"'details' is not in {obj}")
    details = obj["details"]
    if not isinstance(details, str):
        raise ValueError(f"{repr(details)} is not str")
    if "shippingAddressEmail" not in obj:
        raise KeyError(f"'shippingAddressEmail' is not in {obj}")
    shipping_address_email = obj["shippingAddressEmail"]
    if not isinstance(shipping_address_email, str):
        raise ValueError(f"{repr(shipping_address_email)} is not str")
    if "reason" in obj:
        reason = obj["reason"]
        if not isinstance(reason, str):
            raise ValueError(f"{repr(reason)} is not str")
    else:
        reason = None
    if "carrierTrackingId" in obj:
        carrier_tracking_id = obj["carrierTrackingId"]
        if not isinstance(carrier_tracking_id, str):
            raise ValueError(f"{repr(carrier_tracking_id)} is not str")
    else:
        carrier_tracking_id = None
    if "carrierType" in obj:
        carrier_type = obj["carrierType"]
        if not isinstance(carrier_type, str):
            raise ValueError(f"{repr(carrier_type)} is not str")
    else:
        carrier_type = None
    if "shippingAddressCountry" in obj:
        shipping_address_country = obj["shippingAddressCountry"]
        shipping_address_country = _deserialize_country(shipping_address_country)
    else:
        shipping_address_country = None
    if "shippingAddressCity" in obj:
        shipping_address_city = obj["shippingAddressCity"]
        if not isinstance(shipping_address_city, str):
            raise ValueError(f"{repr(shipping_address_city)} is not str")
    else:
        shipping_address_city = None
    if "shippingAddressZip" in obj:
        shipping_address_zip = obj["shippingAddressZip"]
        if not isinstance(shipping_address_zip, str):
            raise ValueError(f"{repr(shipping_address_zip)} is not str")
    else:
        shipping_address_zip = None
    if "shippingAddressState" in obj:
        shipping_address_state = obj["shippingAddressState"]
        if not isinstance(shipping_address_state, str):
            raise ValueError(f"{repr(shipping_address_state)} is not str")
    else:
        shipping_address_state = None
    if "shippingAddressStreet" in obj:
        shipping_address_street = obj["shippingAddressStreet"]
        if not isinstance(shipping_address_street, str):
            raise ValueError(f"{repr(shipping_address_street)} is not str")
    else:
        shipping_address_street = None
    if "shippingAddressPhone" in obj:
        shipping_address_phone = obj["shippingAddressPhone"]
        if not isinstance(shipping_address_phone, str):
            raise ValueError(f"{repr(shipping_address_phone)} is not str")
    else:
        shipping_address_phone = None
    if "shippingAddressFirstname" in obj:
        shipping_address_firstname = obj["shippingAddressFirstname"]
        if not isinstance(shipping_address_firstname, str):
            raise ValueError(f"{repr(shipping_address_firstname)} is not str")
    else:
        shipping_address_firstname = None
    if "shippingAddressLastname" in obj:
        shipping_address_lastname = obj["shippingAddressLastname"]
        if not isinstance(shipping_address_lastname, str):
            raise ValueError(f"{repr(shipping_address_lastname)} is not str")
    else:
        shipping_address_lastname = None
    if "attachments" in obj:
        attachments = obj["attachments"]
        if not isinstance(attachments, list):
            raise ValueError(f"{repr(attachments)} is not list")
        for i, item in enumerate(attachments):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        attachments = None
    return ConfirmPaymentwallDeliveryBody(transaction_id, delivery_type, delivery_status, estimated_delivery_datetime, estimated_update_datetime, refundable, details, shipping_address_email, reason, carrier_tracking_id, carrier_type, shipping_address_country, shipping_address_city, shipping_address_zip, shipping_address_state, shipping_address_street, shipping_address_phone, shipping_address_firstname, shipping_address_lastname, attachments)
