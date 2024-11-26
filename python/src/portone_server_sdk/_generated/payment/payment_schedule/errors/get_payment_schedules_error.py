from dataclasses import dataclass
from ....._portone_error import PortOneError
@dataclass
class GetPaymentSchedulesError(PortOneError):
    pass
