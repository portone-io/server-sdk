from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_user_defined_formula_results import PlatformUserDefinedFormulaResults, _deserialize_platform_user_defined_formula_results, _serialize_platform_user_defined_formula_results

@dataclass
class PlatformOrderSettlementAmount:
    """정산 금액 정보

    정산 금액과 정산 금액 계산에 사용된 금액 정보들 입니다.
    """
    settlement: int
    """정산 금액
    (int64)
    """
    settlement_tax_free: int
    """정산 면세 금액
    (int64)
    """
    payment: int
    """결제 금액
    (int64)
    """
    payment_vat: int
    """결제 금액 부가세
    (int64)
    """
    payment_vat_burden: int
    """결제 금액 부가세 부담금액

    참조된 계약의 결제 금액 부가세 감액 여부에 따라 false인 경우 0원, true인 경우 결제 금액 부가세입니다.
    (int64)
    """
    payment_tax_free: int
    """결제 면세 금액
    (int64)
    """
    payment_supply: int
    """결제 공급가액
    (int64)
    """
    order: int
    """주문 금액
    (int64)
    """
    order_tax_free: int
    """면세 주문 금액
    (int64)
    """
    platform_fee: int
    """중개 수수료
    (int64)
    """
    platform_fee_vat: int
    """중개 수수료 부가세
    (int64)
    """
    additional_fee: int
    """추가 수수료
    (int64)
    """
    additional_fee_vat: int
    """추가 수수료 부가세
    (int64)
    """
    discount: int
    """할인 금액
    (int64)
    """
    discount_tax_free: int
    """면세 할인 금액
    (int64)
    """
    discount_share: int
    """할인 분담 금액
    (int64)
    """
    discount_share_tax_free: int
    """면세 할인 분담 금액
    (int64)
    """
    user_defined_formulas: PlatformUserDefinedFormulaResults
    """사용자 정의 수식 결과
    """


def _serialize_platform_order_settlement_amount(obj: PlatformOrderSettlementAmount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["settlement"] = obj.settlement
    entity["settlementTaxFree"] = obj.settlement_tax_free
    entity["payment"] = obj.payment
    entity["paymentVat"] = obj.payment_vat
    entity["paymentVatBurden"] = obj.payment_vat_burden
    entity["paymentTaxFree"] = obj.payment_tax_free
    entity["paymentSupply"] = obj.payment_supply
    entity["order"] = obj.order
    entity["orderTaxFree"] = obj.order_tax_free
    entity["platformFee"] = obj.platform_fee
    entity["platformFeeVat"] = obj.platform_fee_vat
    entity["additionalFee"] = obj.additional_fee
    entity["additionalFeeVat"] = obj.additional_fee_vat
    entity["discount"] = obj.discount
    entity["discountTaxFree"] = obj.discount_tax_free
    entity["discountShare"] = obj.discount_share
    entity["discountShareTaxFree"] = obj.discount_share_tax_free
    entity["userDefinedFormulas"] = _serialize_platform_user_defined_formula_results(obj.user_defined_formulas)
    return entity


def _deserialize_platform_order_settlement_amount(obj: Any) -> PlatformOrderSettlementAmount:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "settlement" not in obj:
        raise KeyError("Missing required field 'settlement'")
    settlement = obj["settlement"]
    if not isinstance(settlement, int):
        raise ValueError("Expected int for settlement")
    if "settlementTaxFree" not in obj:
        raise KeyError("Missing required field 'settlementTaxFree'")
    settlement_tax_free = obj["settlementTaxFree"]
    if not isinstance(settlement_tax_free, int):
        raise ValueError("Expected int for settlement_tax_free")
    if "payment" not in obj:
        raise KeyError("Missing required field 'payment'")
    payment = obj["payment"]
    if not isinstance(payment, int):
        raise ValueError("Expected int for payment")
    if "paymentVat" not in obj:
        raise KeyError("Missing required field 'paymentVat'")
    payment_vat = obj["paymentVat"]
    if not isinstance(payment_vat, int):
        raise ValueError("Expected int for payment_vat")
    if "paymentVatBurden" not in obj:
        raise KeyError("Missing required field 'paymentVatBurden'")
    payment_vat_burden = obj["paymentVatBurden"]
    if not isinstance(payment_vat_burden, int):
        raise ValueError("Expected int for payment_vat_burden")
    if "paymentTaxFree" not in obj:
        raise KeyError("Missing required field 'paymentTaxFree'")
    payment_tax_free = obj["paymentTaxFree"]
    if not isinstance(payment_tax_free, int):
        raise ValueError("Expected int for payment_tax_free")
    if "paymentSupply" not in obj:
        raise KeyError("Missing required field 'paymentSupply'")
    payment_supply = obj["paymentSupply"]
    if not isinstance(payment_supply, int):
        raise ValueError("Expected int for payment_supply")
    if "order" not in obj:
        raise KeyError("Missing required field 'order'")
    order = obj["order"]
    if not isinstance(order, int):
        raise ValueError("Expected int for order")
    if "orderTaxFree" not in obj:
        raise KeyError("Missing required field 'orderTaxFree'")
    order_tax_free = obj["orderTaxFree"]
    if not isinstance(order_tax_free, int):
        raise ValueError("Expected int for order_tax_free")
    if "platformFee" not in obj:
        raise KeyError("Missing required field 'platformFee'")
    platform_fee = obj["platformFee"]
    if not isinstance(platform_fee, int):
        raise ValueError("Expected int for platform_fee")
    if "platformFeeVat" not in obj:
        raise KeyError("Missing required field 'platformFeeVat'")
    platform_fee_vat = obj["platformFeeVat"]
    if not isinstance(platform_fee_vat, int):
        raise ValueError("Expected int for platform_fee_vat")
    if "additionalFee" not in obj:
        raise KeyError("Missing required field 'additionalFee'")
    additional_fee = obj["additionalFee"]
    if not isinstance(additional_fee, int):
        raise ValueError("Expected int for additional_fee")
    if "additionalFeeVat" not in obj:
        raise KeyError("Missing required field 'additionalFeeVat'")
    additional_fee_vat = obj["additionalFeeVat"]
    if not isinstance(additional_fee_vat, int):
        raise ValueError("Expected int for additional_fee_vat")
    if "discount" not in obj:
        raise KeyError("Missing required field 'discount'")
    discount = obj["discount"]
    if not isinstance(discount, int):
        raise ValueError("Expected int for discount")
    if "discountTaxFree" not in obj:
        raise KeyError("Missing required field 'discountTaxFree'")
    discount_tax_free = obj["discountTaxFree"]
    if not isinstance(discount_tax_free, int):
        raise ValueError("Expected int for discount_tax_free")
    if "discountShare" not in obj:
        raise KeyError("Missing required field 'discountShare'")
    discount_share = obj["discountShare"]
    if not isinstance(discount_share, int):
        raise ValueError("Expected int for discount_share")
    if "discountShareTaxFree" not in obj:
        raise KeyError("Missing required field 'discountShareTaxFree'")
    discount_share_tax_free = obj["discountShareTaxFree"]
    if not isinstance(discount_share_tax_free, int):
        raise ValueError("Expected int for discount_share_tax_free")
    if "userDefinedFormulas" not in obj:
        raise KeyError("Missing required field 'userDefinedFormulas'")
    user_defined_formulas = obj["userDefinedFormulas"]
    user_defined_formulas = _deserialize_platform_user_defined_formula_results(user_defined_formulas)
    return PlatformOrderSettlementAmount(settlement, settlement_tax_free, payment, payment_vat, payment_vat_burden, payment_tax_free, payment_supply, order, order_tax_free, platform_fee, platform_fee_vat, additional_fee, additional_fee_vat, discount, discount_tax_free, discount_share, discount_share_tax_free, user_defined_formulas)
