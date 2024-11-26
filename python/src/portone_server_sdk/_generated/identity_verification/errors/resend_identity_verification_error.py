from dataclasses import dataclass
from ...._portone_error import PortOneError
@dataclass
class ResendIdentityVerificationError(PortOneError):
    pass
