from dataclasses import dataclass
from ....._portone_error import ApiError
@dataclass
class CreatePaymentScheduleError(ApiError):
    pass
