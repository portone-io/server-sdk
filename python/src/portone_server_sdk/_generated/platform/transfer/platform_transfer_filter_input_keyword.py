from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformTransferFilterInputKeyword:
    """정산건 검색 키워드 입력 정보

    검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 정산건만 조회합니다. 하나의 하위 필드에만 값을 명시하여 요청합니다.
    """
    all: Optional[str] = field(default=None)
    """해당 값이 포함된 정보를 가진 정산건만 조회합니다.
    """
    payment_id: Optional[str] = field(default=None)
    """해당 값이랑 일치하는 paymentId 를 가진 정산건만 조회합니다.
    """
    transfer_id: Optional[str] = field(default=None)
    """해당 값이랑 일치하는 transferId 를 가진 정산건만 조회합니다.
    """
    transfer_memo: Optional[str] = field(default=None)
    """해당 값이 포함된 transferMemo 를 가진 정산건만 조회합니다.
    """
    product_id: Optional[str] = field(default=None)
    """해당 값이랑 일치하는 productId 를 가진 정산건만 조회합니다.
    """
    product_name: Optional[str] = field(default=None)
    """해당 값이랑 일치하는 productName 을 가진 정산건만 조회합니다.
    """
    partner_id: Optional[str] = field(default=None)
    """해당 값이랑 일치하는 partnerId 를 가진 정산건만 조회합니다.
    """
    partner_name: Optional[str] = field(default=None)
    """해당 값이 포함된 partnerName 을 가진 정산건만 조회합니다.
    """
    partner_memo: Optional[str] = field(default=None)
    """해당 값이 포함된 partnerMemo 를 가진 정산건만 조회합니다.
    """


def _serialize_platform_transfer_filter_input_keyword(obj: PlatformTransferFilterInputKeyword) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.all is not None:
        entity["all"] = obj.all
    if obj.payment_id is not None:
        entity["paymentId"] = obj.payment_id
    if obj.transfer_id is not None:
        entity["transferId"] = obj.transfer_id
    if obj.transfer_memo is not None:
        entity["transferMemo"] = obj.transfer_memo
    if obj.product_id is not None:
        entity["productId"] = obj.product_id
    if obj.product_name is not None:
        entity["productName"] = obj.product_name
    if obj.partner_id is not None:
        entity["partnerId"] = obj.partner_id
    if obj.partner_name is not None:
        entity["partnerName"] = obj.partner_name
    if obj.partner_memo is not None:
        entity["partnerMemo"] = obj.partner_memo
    return entity


def _deserialize_platform_transfer_filter_input_keyword(obj: Any) -> PlatformTransferFilterInputKeyword:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "all" in obj:
        all = obj["all"]
        if not isinstance(all, str):
            raise ValueError(f"{repr(all)} is not str")
    else:
        all = None
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
    if "transferMemo" in obj:
        transfer_memo = obj["transferMemo"]
        if not isinstance(transfer_memo, str):
            raise ValueError(f"{repr(transfer_memo)} is not str")
    else:
        transfer_memo = None
    if "productId" in obj:
        product_id = obj["productId"]
        if not isinstance(product_id, str):
            raise ValueError(f"{repr(product_id)} is not str")
    else:
        product_id = None
    if "productName" in obj:
        product_name = obj["productName"]
        if not isinstance(product_name, str):
            raise ValueError(f"{repr(product_name)} is not str")
    else:
        product_name = None
    if "partnerId" in obj:
        partner_id = obj["partnerId"]
        if not isinstance(partner_id, str):
            raise ValueError(f"{repr(partner_id)} is not str")
    else:
        partner_id = None
    if "partnerName" in obj:
        partner_name = obj["partnerName"]
        if not isinstance(partner_name, str):
            raise ValueError(f"{repr(partner_name)} is not str")
    else:
        partner_name = None
    if "partnerMemo" in obj:
        partner_memo = obj["partnerMemo"]
        if not isinstance(partner_memo, str):
            raise ValueError(f"{repr(partner_memo)} is not str")
    else:
        partner_memo = None
    return PlatformTransferFilterInputKeyword(all, payment_id, transfer_id, transfer_memo, product_id, product_name, partner_id, partner_name, partner_memo)
