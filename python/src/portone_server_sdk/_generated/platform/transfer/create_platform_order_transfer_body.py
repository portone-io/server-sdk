from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_additional_fee import CreatePlatformOrderTransferBodyAdditionalFee, _deserialize_create_platform_order_transfer_body_additional_fee, _serialize_create_platform_order_transfer_body_additional_fee
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_discount import CreatePlatformOrderTransferBodyDiscount, _deserialize_create_platform_order_transfer_body_discount, _serialize_create_platform_order_transfer_body_discount
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_external_payment_detail import CreatePlatformOrderTransferBodyExternalPaymentDetail, _deserialize_create_platform_order_transfer_body_external_payment_detail, _serialize_create_platform_order_transfer_body_external_payment_detail
from portone_server_sdk._generated.platform.transfer.create_platform_order_transfer_body_order_detail import CreatePlatformOrderTransferBodyOrderDetail, _deserialize_create_platform_order_transfer_body_order_detail, _serialize_create_platform_order_transfer_body_order_detail
from portone_server_sdk._generated.platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value
from portone_server_sdk._generated.platform.transfer.transfer_parameters import TransferParameters, _deserialize_transfer_parameters, _serialize_transfer_parameters

@dataclass
class CreatePlatformOrderTransferBody:
    """주문 정산건 생성을 위한 입력 정보
    """
    partner_id: str
    """파트너 아이디
    """
    payment_id: str
    """결제 아이디
    """
    order_detail: CreatePlatformOrderTransferBodyOrderDetail
    """주문 정보
    """
    discounts: list[CreatePlatformOrderTransferBodyDiscount]
    """할인 정보
    """
    additional_fees: list[CreatePlatformOrderTransferBodyAdditionalFee]
    """추가 수수료 정보
    """
    contract_id: Optional[str]
    """계약 아이디

    기본값은 파트너의 기본 계약 아이디 입니다.
    """
    memo: Optional[str]
    """메모
    """
    tax_free_amount: Optional[int]
    """주문 면세 금액

    주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
    (int64)
    """
    settlement_start_date: Optional[str]
    """정산 시작일

    기본값은 결제 일시 입니다.
    """
    external_payment_detail: Optional[CreatePlatformOrderTransferBodyExternalPaymentDetail]
    """외부 결제 상세 정보

    해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
    """
    is_for_test: Optional[bool]
    """테스트 모드 여부

    기본값은 false 입니다.
    """
    parameters: Optional[TransferParameters]
    """정산 파라미터 (실험기능)
    """
    user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]]
    """사용자 정의 속성
    """


def _serialize_create_platform_order_transfer_body(obj: CreatePlatformOrderTransferBody) -> Any:
    entity = {}
    entity["partnerId"] = obj.partner_id
    entity["paymentId"] = obj.payment_id
    entity["orderDetail"] = _serialize_create_platform_order_transfer_body_order_detail(obj.order_detail)
    entity["discounts"] = list(map(_serialize_create_platform_order_transfer_body_discount, obj.discounts))
    entity["additionalFees"] = list(map(_serialize_create_platform_order_transfer_body_additional_fee, obj.additional_fees))
    if obj.contract_id is not None:
        entity["contractId"] = obj.contract_id
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.tax_free_amount is not None:
        entity["taxFreeAmount"] = obj.tax_free_amount
    if obj.settlement_start_date is not None:
        entity["settlementStartDate"] = obj.settlement_start_date
    if obj.external_payment_detail is not None:
        entity["externalPaymentDetail"] = _serialize_create_platform_order_transfer_body_external_payment_detail(obj.external_payment_detail)
    if obj.is_for_test is not None:
        entity["isForTest"] = obj.is_for_test
    if obj.parameters is not None:
        entity["parameters"] = _serialize_transfer_parameters(obj.parameters)
    if obj.user_defined_properties is not None:
        entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    return entity


def _deserialize_create_platform_order_transfer_body(obj: Any) -> CreatePlatformOrderTransferBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partnerId" not in obj:
        raise KeyError(f"'partnerId' is not in {obj}")
    partner_id = obj["partnerId"]
    if not isinstance(partner_id, str):
        raise ValueError(f"{repr(partner_id)} is not str")
    if "paymentId" not in obj:
        raise KeyError(f"'paymentId' is not in {obj}")
    payment_id = obj["paymentId"]
    if not isinstance(payment_id, str):
        raise ValueError(f"{repr(payment_id)} is not str")
    if "orderDetail" not in obj:
        raise KeyError(f"'orderDetail' is not in {obj}")
    order_detail = obj["orderDetail"]
    order_detail = _deserialize_create_platform_order_transfer_body_order_detail(order_detail)
    if "discounts" not in obj:
        raise KeyError(f"'discounts' is not in {obj}")
    discounts = obj["discounts"]
    if not isinstance(discounts, list):
        raise ValueError(f"{repr(discounts)} is not list")
    for i, item in enumerate(discounts):
        item = _deserialize_create_platform_order_transfer_body_discount(item)
        discounts[i] = item
    if "additionalFees" not in obj:
        raise KeyError(f"'additionalFees' is not in {obj}")
    additional_fees = obj["additionalFees"]
    if not isinstance(additional_fees, list):
        raise ValueError(f"{repr(additional_fees)} is not list")
    for i, item in enumerate(additional_fees):
        item = _deserialize_create_platform_order_transfer_body_additional_fee(item)
        additional_fees[i] = item
    if "contractId" in obj:
        contract_id = obj["contractId"]
        if not isinstance(contract_id, str):
            raise ValueError(f"{repr(contract_id)} is not str")
    else:
        contract_id = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
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
    if "externalPaymentDetail" in obj:
        external_payment_detail = obj["externalPaymentDetail"]
        external_payment_detail = _deserialize_create_platform_order_transfer_body_external_payment_detail(external_payment_detail)
    else:
        external_payment_detail = None
    if "isForTest" in obj:
        is_for_test = obj["isForTest"]
        if not isinstance(is_for_test, bool):
            raise ValueError(f"{repr(is_for_test)} is not bool")
    else:
        is_for_test = None
    if "parameters" in obj:
        parameters = obj["parameters"]
        parameters = _deserialize_transfer_parameters(parameters)
    else:
        parameters = None
    if "userDefinedProperties" in obj:
        user_defined_properties = obj["userDefinedProperties"]
        if not isinstance(user_defined_properties, list):
            raise ValueError(f"{repr(user_defined_properties)} is not list")
        for i, item in enumerate(user_defined_properties):
            item = _deserialize_platform_user_defined_property_key_value(item)
            user_defined_properties[i] = item
    else:
        user_defined_properties = None
    return CreatePlatformOrderTransferBody(partner_id, payment_id, order_detail, discounts, additional_fees, contract_id, memo, tax_free_amount, settlement_start_date, external_payment_detail, is_for_test, parameters, user_defined_properties)
