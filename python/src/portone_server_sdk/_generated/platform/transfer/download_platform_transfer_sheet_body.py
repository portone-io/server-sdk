from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.platform_transfer_filter_input import PlatformTransferFilterInput, _deserialize_platform_transfer_filter_input, _serialize_platform_transfer_filter_input

@dataclass
class DownloadPlatformTransferSheetBody:
    filter: Optional[PlatformTransferFilterInput] = field(default=None)
    """컬럼 키 목록

    - TRANSFER_MEMO:  메모
    - TRANSFER_TYPE: 정산 유형
    - TRANSFER_STATUS:  상태
    - TRANSFER_ID: 정산 아이디
    - TRANSFER_SETTLEMENT_DATE:  정산일
    - TRANSFER_SETTLEMENT_AMOUNT: 정산 금액
    - TRANSFER_SETTLEMENT_TAX_FREE_AMOUNT: 정산 면세액
    - TRANSFER_SETTLEMENT_CURRENCY: 정산 통화
    - TRANSFER_SETTLEMENT_START_DATE: 정산 시작일
    - TRANSFER_ORDER_NAME:  주문명
    - TRANSFER_ORDER_AMOUNT: 주문 금액
    - TRANSFER_ORDER_TAX_FREE_AMOUNT: 주문 면세액
    - TRANSFER_PAYMENT_ID: 주문 번호
    - TRANSFER_PAYMENT_METHOD: 결제 수단
    - TRANSFER_PAYMENT_AMOUNT: 결제 금액
    - TRANSFER_PAYMENT_SUPPLY_AMOUNT: 결제 공급가액
    - TRANSFER_PAYMENT_VAT_AMOUNT: 결제 부가세액
    - TRANSFER_PAYMENT_TAX_FREE_AMOUNT: 결제 면세액
    - TRANSFER_PAYMENT_VAT_BURDEN_AMOUNT: 결제 부가세 부담금
    - TRANSFER_PLATFORM_FEE:  중개수수료
    - TRANSFER_PLATFORM_FEE_VAT: 중개수수료 부가세 부담금
    - TRANSFER_CONTRACT_ID: 계약 아이디
    - TRANSFER_CONTRACT_NAME: 계약 이름
    - TRANSFER_DISCOUNT_AMOUNT: 할인 금액
    - TRANSFER_DISCOUNT_TAX_FREE_AMOUNT: 할인 면세액
    - TRANSFER_DISCOUNT_SHARE_AMOUNT: 할인 분담금
    - TRANSFER_DISCOUNT_SHARE_TAX_FREE_AMOUNT: 할인 면세 분담금
    - TRANSFER_ADDITIONAL_FEE:  추가수수료
    - TRANSFER_ADDITIONAL_FEE_VAT: 추가수수료 부가세 부담금
    - TRANSFER_{UserDefinedProperty.Key}
    - FORMULA_{UserDefinedFormula.Key}
    - PARTNER_* : 파트너 컬럼 키 사용 가능(w/o PARTNER_STATUS_UPDATED_AT)
    """
    fields: Optional[list[str]] = field(default=None)


def _serialize_download_platform_transfer_sheet_body(obj: DownloadPlatformTransferSheetBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.filter is not None:
        entity["filter"] = _serialize_platform_transfer_filter_input(obj.filter)
    if obj.fields is not None:
        entity["fields"] = obj.fields
    return entity


def _deserialize_download_platform_transfer_sheet_body(obj: Any) -> DownloadPlatformTransferSheetBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "filter" in obj:
        filter = obj["filter"]
        filter = _deserialize_platform_transfer_filter_input(filter)
    else:
        filter = None
    if "fields" in obj:
        fields = obj["fields"]
        if not isinstance(fields, list):
            raise ValueError(f"{repr(fields)} is not list")
        for i, item in enumerate(fields):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        fields = None
    return DownloadPlatformTransferSheetBody(filter, fields)
