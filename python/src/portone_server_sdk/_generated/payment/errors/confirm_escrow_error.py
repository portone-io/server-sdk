from dataclasses import dataclass
from ...._portone_error import ApiError
@dataclass
class ConfirmEscrowError(ApiError):
    pass
