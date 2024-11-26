from dataclasses import dataclass
from ...._portone_error import PortOneError
@dataclass
class PreRegisterPaymentError(PortOneError):
    pass
