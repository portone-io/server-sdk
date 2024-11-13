from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformOrderSettlementAmount:
    """정산 금액 정보

    정산 금액과 정산 금액 계산에 사용된 금액 정보들 입니다.
    """
    settlement: int
    """정산 금액
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
    tax_free: int
    """결제 면세 금액

    해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentTaxFree 필드를 사용해주세요.
    (int64)
    """
    supply: int
    """결제 공급가액

    해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentSupply 필드를 사용해주세요.
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


def _serialize_platform_order_settlement_amount(obj: PlatformOrderSettlementAmount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["settlement"] = obj.settlement
    entity["payment"] = obj.payment
    entity["paymentVat"] = obj.payment_vat
    entity["paymentVatBurden"] = obj.payment_vat_burden
    entity["taxFree"] = obj.tax_free
    entity["supply"] = obj.supply
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
    return entity


def _deserialize_platform_order_settlement_amount(obj: Any) -> PlatformOrderSettlementAmount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "settlement" not in obj:
        raise KeyError(f"'settlement' is not in {obj}")
    settlement = obj["settlement"]
    if not isinstance(settlement, int):
        raise ValueError(f"{repr(settlement)} is not int")
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    if not isinstance(payment, int):
        raise ValueError(f"{repr(payment)} is not int")
    if "paymentVat" not in obj:
        raise KeyError(f"'paymentVat' is not in {obj}")
    payment_vat = obj["paymentVat"]
    if not isinstance(payment_vat, int):
        raise ValueError(f"{repr(payment_vat)} is not int")
    if "paymentVatBurden" not in obj:
        raise KeyError(f"'paymentVatBurden' is not in {obj}")
    payment_vat_burden = obj["paymentVatBurden"]
    if not isinstance(payment_vat_burden, int):
        raise ValueError(f"{repr(payment_vat_burden)} is not int")
    if "taxFree" not in obj:
        raise KeyError(f"'taxFree' is not in {obj}")
    tax_free = obj["taxFree"]
    if not isinstance(tax_free, int):
        raise ValueError(f"{repr(tax_free)} is not int")
    if "supply" not in obj:
        raise KeyError(f"'supply' is not in {obj}")
    supply = obj["supply"]
    if not isinstance(supply, int):
        raise ValueError(f"{repr(supply)} is not int")
    if "paymentTaxFree" not in obj:
        raise KeyError(f"'paymentTaxFree' is not in {obj}")
    payment_tax_free = obj["paymentTaxFree"]
    if not isinstance(payment_tax_free, int):
        raise ValueError(f"{repr(payment_tax_free)} is not int")
    if "paymentSupply" not in obj:
        raise KeyError(f"'paymentSupply' is not in {obj}")
    payment_supply = obj["paymentSupply"]
    if not isinstance(payment_supply, int):
        raise ValueError(f"{repr(payment_supply)} is not int")
    if "order" not in obj:
        raise KeyError(f"'order' is not in {obj}")
    order = obj["order"]
    if not isinstance(order, int):
        raise ValueError(f"{repr(order)} is not int")
    if "orderTaxFree" not in obj:
        raise KeyError(f"'orderTaxFree' is not in {obj}")
    order_tax_free = obj["orderTaxFree"]
    if not isinstance(order_tax_free, int):
        raise ValueError(f"{repr(order_tax_free)} is not int")
    if "platformFee" not in obj:
        raise KeyError(f"'platformFee' is not in {obj}")
    platform_fee = obj["platformFee"]
    if not isinstance(platform_fee, int):
        raise ValueError(f"{repr(platform_fee)} is not int")
    if "platformFeeVat" not in obj:
        raise KeyError(f"'platformFeeVat' is not in {obj}")
    platform_fee_vat = obj["platformFeeVat"]
    if not isinstance(platform_fee_vat, int):
        raise ValueError(f"{repr(platform_fee_vat)} is not int")
    if "additionalFee" not in obj:
        raise KeyError(f"'additionalFee' is not in {obj}")
    additional_fee = obj["additionalFee"]
    if not isinstance(additional_fee, int):
        raise ValueError(f"{repr(additional_fee)} is not int")
    if "additionalFeeVat" not in obj:
        raise KeyError(f"'additionalFeeVat' is not in {obj}")
    additional_fee_vat = obj["additionalFeeVat"]
    if not isinstance(additional_fee_vat, int):
        raise ValueError(f"{repr(additional_fee_vat)} is not int")
    if "discount" not in obj:
        raise KeyError(f"'discount' is not in {obj}")
    discount = obj["discount"]
    if not isinstance(discount, int):
        raise ValueError(f"{repr(discount)} is not int")
    if "discountTaxFree" not in obj:
        raise KeyError(f"'discountTaxFree' is not in {obj}")
    discount_tax_free = obj["discountTaxFree"]
    if not isinstance(discount_tax_free, int):
        raise ValueError(f"{repr(discount_tax_free)} is not int")
    if "discountShare" not in obj:
        raise KeyError(f"'discountShare' is not in {obj}")
    discount_share = obj["discountShare"]
    if not isinstance(discount_share, int):
        raise ValueError(f"{repr(discount_share)} is not int")
    if "discountShareTaxFree" not in obj:
        raise KeyError(f"'discountShareTaxFree' is not in {obj}")
    discount_share_tax_free = obj["discountShareTaxFree"]
    if not isinstance(discount_share_tax_free, int):
        raise ValueError(f"{repr(discount_share_tax_free)} is not int")
    return PlatformOrderSettlementAmount(settlement, payment, payment_vat, payment_vat_burden, tax_free, supply, payment_tax_free, payment_supply, order, order_tax_free, platform_fee, platform_fee_vat, additional_fee, additional_fee_vat, discount, discount_tax_free, discount_share, discount_share_tax_free)
