from __future__ import annotations
from typing import Any, Literal, Optional

PaymentLogisticsCompany = Literal["LOTTE", "LOGEN", "DONGWON", "POST", "CJ", "HANJIN", "DAESIN", "ILYANG", "KYUNGDONG", "CHUNIL", "POST_REGISTERED", "GS", "WOORI", "HAPDONG", "FEDEX", "UPS", "GSM_NTON", "SUNGWON", "LX_PANTOS", "ACI", "CJ_INTL", "USPS", "EMS", "DHL", "KGL", "GOODSTOLUCK", "KUNYOUNG", "SLX", "SF", "ETC"]
"""물류 회사
"""


def _serialize_payment_logistics_company(obj: PaymentLogisticsCompany) -> Any:
    return obj


def _deserialize_payment_logistics_company(obj: Any) -> PaymentLogisticsCompany:
    if obj not in ["LOTTE", "LOGEN", "DONGWON", "POST", "CJ", "HANJIN", "DAESIN", "ILYANG", "KYUNGDONG", "CHUNIL", "POST_REGISTERED", "GS", "WOORI", "HAPDONG", "FEDEX", "UPS", "GSM_NTON", "SUNGWON", "LX_PANTOS", "ACI", "CJ_INTL", "USPS", "EMS", "DHL", "KGL", "GOODSTOLUCK", "KUNYOUNG", "SLX", "SF", "ETC"]:
        raise ValueError(f"{repr(obj)} is not PaymentLogisticsCompany")
    return obj
