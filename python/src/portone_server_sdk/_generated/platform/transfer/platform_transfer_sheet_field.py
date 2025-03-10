from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformTransferSheetField = Union[Literal["STATUS", "TRANSFER_ID", "PARTNER_NAME", "SETTLEMENT_DATE", "SETTLEMENT_START_DATE", "TYPE", "PAYMENT_ID", "ORDER_NAME", "PAYMENT_METHOD", "SETTLEMENT_AMOUNT", "SETTLEMENT_ORDER_AMOUNT", "SETTLEMENT_ORDER_TAX_FREE_AMOUNT", "SETTLEMENT_PAYMENT_AMOUNT", "SETTLEMENT_PAYMENT_VAT_AMOUNT", "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT", "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT", "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT", "SETTLEMENT_PLATFORM_FEE_AMOUNT", "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT", "SETTLEMENT_DISCOUNT_AMOUNT", "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT", "SETTLEMENT_DISCOUNT_SHARE_AMOUNT", "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT", "SETTLEMENT_ADDITIONAL_FEE_AMOUNT", "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT", "SETTLEMENT_CURRENCY", "PARTNER_TYPE", "PARTNER_TAXATION_TYPE", "PARTNER_INCOME_TYPE", "PARTNER_TAXATION_TYPE_OR_INCOME_TYPE", "PARTNER_ID", "MEMO"], str]
"""다운로드 할 시트 컬럼
"""


def _serialize_platform_transfer_sheet_field(obj: PlatformTransferSheetField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_transfer_sheet_field(obj: Any) -> PlatformTransferSheetField:
    return obj
