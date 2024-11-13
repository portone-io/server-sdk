from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentLogisticsCompany = Union[Literal["LOTTE", "LOGEN", "DONGWON", "POST", "CJ", "HANJIN", "DAESIN", "ILYANG", "KYUNGDONG", "CHUNIL", "POST_REGISTERED", "GS", "WOORI", "HAPDONG", "FEDEX", "UPS", "GSM_NTON", "SUNGWON", "LX_PANTOS", "ACI", "CJ_INTL", "USPS", "EMS", "DHL", "KGL", "GOODSTOLUCK", "KUNYOUNG", "SLX", "SF", "ETC"], str]
"""물류 회사
"""


def _serialize_payment_logistics_company(obj: PaymentLogisticsCompany) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_logistics_company(obj: Any) -> PaymentLogisticsCompany:
    return obj
