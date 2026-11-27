from dataclasses import dataclass, field
from typing import Optional


@dataclass(init=False)
class PortOneError(Exception):
    """포트원 SDK에서 발생하는 모든 에러의 기본 타입입니다."""

    message: Optional[str] = field(init=False)


class ApiError(PortOneError):
    def __str__(self) -> str:
        return self.message or type(self).__name__
