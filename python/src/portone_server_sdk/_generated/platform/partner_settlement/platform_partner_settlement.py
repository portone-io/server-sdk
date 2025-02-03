from __future__ import annotations
from typing import Any, Optional, Union
from ...platform.partner_settlement.platform_partner_manual_settlement import PlatformPartnerManualSettlement, _deserialize_platform_partner_manual_settlement, _serialize_platform_partner_manual_settlement
from ...platform.partner_settlement.platform_partner_order_cancel_settlement import PlatformPartnerOrderCancelSettlement, _deserialize_platform_partner_order_cancel_settlement, _serialize_platform_partner_order_cancel_settlement
from ...platform.partner_settlement.platform_partner_order_settlement import PlatformPartnerOrderSettlement, _deserialize_platform_partner_order_settlement, _serialize_platform_partner_order_settlement

PlatformPartnerSettlement = Union[PlatformPartnerManualSettlement, PlatformPartnerOrderSettlement, PlatformPartnerOrderCancelSettlement, dict]


def _serialize_platform_partner_settlement(obj: PlatformPartnerSettlement) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformPartnerManualSettlement):
        return _serialize_platform_partner_manual_settlement(obj)
    if isinstance(obj, PlatformPartnerOrderSettlement):
        return _serialize_platform_partner_order_settlement(obj)
    if isinstance(obj, PlatformPartnerOrderCancelSettlement):
        return _serialize_platform_partner_order_cancel_settlement(obj)


def _deserialize_platform_partner_settlement(obj: Any) -> PlatformPartnerSettlement:
    try:
        return _deserialize_platform_partner_manual_settlement(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_order_settlement(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_order_cancel_settlement(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformPartnerSettlement")
