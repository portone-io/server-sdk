from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.platform.platform_contract import PlatformContract, _deserialize_platform_contract, _serialize_platform_contract
from portone_server_sdk._generated.platform.platform_order_settlement_amount import PlatformOrderSettlementAmount, _deserialize_platform_order_settlement_amount, _serialize_platform_order_settlement_amount
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_additional_fee import PlatformOrderTransferAdditionalFee, _deserialize_platform_order_transfer_additional_fee, _serialize_platform_order_transfer_additional_fee
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_cancellation import PlatformOrderTransferCancellation, _deserialize_platform_order_transfer_cancellation, _serialize_platform_order_transfer_cancellation
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_discount import PlatformOrderTransferDiscount, _deserialize_platform_order_transfer_discount, _serialize_platform_order_transfer_discount
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_order_line import PlatformOrderTransferOrderLine, _deserialize_platform_order_transfer_order_line, _serialize_platform_order_transfer_order_line
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner
from portone_server_sdk._generated.platform.transfer.platform_payment import PlatformPayment, _deserialize_platform_payment, _serialize_platform_payment
from portone_server_sdk._generated.platform.transfer.platform_transfer_status import PlatformTransferStatus, _deserialize_platform_transfer_status, _serialize_platform_transfer_status
from portone_server_sdk._generated.platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value
from portone_server_sdk._generated.platform.transfer.transfer_parameters import TransferParameters, _deserialize_transfer_parameters, _serialize_transfer_parameters

@dataclass
class PlatformOrderCancelTransfer:
    """주문 취소 정산건
    """
    type: Literal["ORDER_CANCEL"] = field(repr=False)
    id: str
    """정산건 아이디
    """
    graphql_id: str
    partner: PlatformPartner
    """파트너
    """
    status: PlatformTransferStatus
    """정산 상태
    """
    settlement_date: str
    """정산 일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    settlement_currency: Currency
    """정산 통화
    """
    is_for_test: bool
    """테스트 모드 여부
    """
    user_defined_properties: list[PlatformUserDefinedPropertyKeyValue]
    """사용자 정의 속성
    """
    amount: PlatformOrderSettlementAmount
    """정산 금액 정보
    """
    contract: PlatformContract
    """계약
    """
    payment: PlatformPayment
    """결제 정보
    """
    settlement_start_date: str
    """정산 시작일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    order_lines: list[PlatformOrderTransferOrderLine]
    """주문 항목 리스트
    """
    additional_fees: list[PlatformOrderTransferAdditionalFee]
    """정산 금액 계산 시 사용된 추가 수수료 정보
    """
    discounts: list[PlatformOrderTransferDiscount]
    """정산 금액 계산 시 사용된 할인 정보
    """
    cancellation: PlatformOrderTransferCancellation
    """주문 취소 정보
    """
    parameters: TransferParameters
    """정산 파라미터 (실험기능)
    """
    memo: Optional[str]
    """메모
    """
    payout_id: Optional[str]
    payout_graphql_id: Optional[str]


def _serialize_platform_order_cancel_transfer(obj: PlatformOrderCancelTransfer) -> Any:
    entity = {}
    entity["type"] = "ORDER_CANCEL"
    entity["id"] = obj.id
    entity["graphqlId"] = obj.graphql_id
    entity["partner"] = _serialize_platform_partner(obj.partner)
    entity["status"] = _serialize_platform_transfer_status(obj.status)
    entity["settlementDate"] = obj.settlement_date
    entity["settlementCurrency"] = _serialize_currency(obj.settlement_currency)
    entity["isForTest"] = obj.is_for_test
    entity["userDefinedProperties"] = list(map(_serialize_platform_user_defined_property_key_value, obj.user_defined_properties))
    entity["amount"] = _serialize_platform_order_settlement_amount(obj.amount)
    entity["contract"] = _serialize_platform_contract(obj.contract)
    entity["payment"] = _serialize_platform_payment(obj.payment)
    entity["settlementStartDate"] = obj.settlement_start_date
    entity["orderLines"] = list(map(_serialize_platform_order_transfer_order_line, obj.order_lines))
    entity["additionalFees"] = list(map(_serialize_platform_order_transfer_additional_fee, obj.additional_fees))
    entity["discounts"] = list(map(_serialize_platform_order_transfer_discount, obj.discounts))
    entity["cancellation"] = _serialize_platform_order_transfer_cancellation(obj.cancellation)
    entity["parameters"] = _serialize_transfer_parameters(obj.parameters)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    if obj.payout_graphql_id is not None:
        entity["payoutGraphqlId"] = obj.payout_graphql_id
    return entity


def _deserialize_platform_order_cancel_transfer(obj: Any) -> PlatformOrderCancelTransfer:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ORDER_CANCEL":
        raise ValueError(f"{repr(type)} is not 'ORDER_CANCEL'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "graphqlId" not in obj:
        raise KeyError(f"'graphqlId' is not in {obj}")
    graphql_id = obj["graphqlId"]
    if not isinstance(graphql_id, str):
        raise ValueError(f"{repr(graphql_id)} is not str")
    if "partner" not in obj:
        raise KeyError(f"'partner' is not in {obj}")
    partner = obj["partner"]
    partner = _deserialize_platform_partner(partner)
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_platform_transfer_status(status)
    if "settlementDate" not in obj:
        raise KeyError(f"'settlementDate' is not in {obj}")
    settlement_date = obj["settlementDate"]
    if not isinstance(settlement_date, str):
        raise ValueError(f"{repr(settlement_date)} is not str")
    if "settlementCurrency" not in obj:
        raise KeyError(f"'settlementCurrency' is not in {obj}")
    settlement_currency = obj["settlementCurrency"]
    settlement_currency = _deserialize_currency(settlement_currency)
    if "isForTest" not in obj:
        raise KeyError(f"'isForTest' is not in {obj}")
    is_for_test = obj["isForTest"]
    if not isinstance(is_for_test, bool):
        raise ValueError(f"{repr(is_for_test)} is not bool")
    if "userDefinedProperties" not in obj:
        raise KeyError(f"'userDefinedProperties' is not in {obj}")
    user_defined_properties = obj["userDefinedProperties"]
    if not isinstance(user_defined_properties, list):
        raise ValueError(f"{repr(user_defined_properties)} is not list")
    for i, item in enumerate(user_defined_properties):
        item = _deserialize_platform_user_defined_property_key_value(item)
        user_defined_properties[i] = item
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    amount = _deserialize_platform_order_settlement_amount(amount)
    if "contract" not in obj:
        raise KeyError(f"'contract' is not in {obj}")
    contract = obj["contract"]
    contract = _deserialize_platform_contract(contract)
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    payment = _deserialize_platform_payment(payment)
    if "settlementStartDate" not in obj:
        raise KeyError(f"'settlementStartDate' is not in {obj}")
    settlement_start_date = obj["settlementStartDate"]
    if not isinstance(settlement_start_date, str):
        raise ValueError(f"{repr(settlement_start_date)} is not str")
    if "orderLines" not in obj:
        raise KeyError(f"'orderLines' is not in {obj}")
    order_lines = obj["orderLines"]
    if not isinstance(order_lines, list):
        raise ValueError(f"{repr(order_lines)} is not list")
    for i, item in enumerate(order_lines):
        item = _deserialize_platform_order_transfer_order_line(item)
        order_lines[i] = item
    if "additionalFees" not in obj:
        raise KeyError(f"'additionalFees' is not in {obj}")
    additional_fees = obj["additionalFees"]
    if not isinstance(additional_fees, list):
        raise ValueError(f"{repr(additional_fees)} is not list")
    for i, item in enumerate(additional_fees):
        item = _deserialize_platform_order_transfer_additional_fee(item)
        additional_fees[i] = item
    if "discounts" not in obj:
        raise KeyError(f"'discounts' is not in {obj}")
    discounts = obj["discounts"]
    if not isinstance(discounts, list):
        raise ValueError(f"{repr(discounts)} is not list")
    for i, item in enumerate(discounts):
        item = _deserialize_platform_order_transfer_discount(item)
        discounts[i] = item
    if "cancellation" not in obj:
        raise KeyError(f"'cancellation' is not in {obj}")
    cancellation = obj["cancellation"]
    cancellation = _deserialize_platform_order_transfer_cancellation(cancellation)
    if "parameters" not in obj:
        raise KeyError(f"'parameters' is not in {obj}")
    parameters = obj["parameters"]
    parameters = _deserialize_transfer_parameters(parameters)
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    if "payoutGraphqlId" in obj:
        payout_graphql_id = obj["payoutGraphqlId"]
        if not isinstance(payout_graphql_id, str):
            raise ValueError(f"{repr(payout_graphql_id)} is not str")
    else:
        payout_graphql_id = None
    return PlatformOrderCancelTransfer(type, id, graphql_id, partner, status, settlement_date, settlement_currency, is_for_test, user_defined_properties, amount, contract, payment, settlement_start_date, order_lines, additional_fees, discounts, cancellation, parameters, memo, payout_id, payout_graphql_id)
