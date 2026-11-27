from dataclasses import dataclass
from ....._portone_error import ApiError
@dataclass
class GetCashReceiptError(ApiError):
    pass
