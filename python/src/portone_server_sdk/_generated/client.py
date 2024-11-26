from __future__ import annotations
from typing import Optional
from httpx import AsyncClient
from .auth.client import AuthClient
from .platform.client import PlatformClient
from .identity_verification.client import IdentityVerificationClient
from .payment.client import PaymentClient
from .pg_specific.client import PgSpecificClient

class PortOneClient:
    _secret: str
    _store_id: Optional[str]
    _base_url: str
    _client: AsyncClient
    auth: AuthClient
    platform: PlatformClient
    identity_verification: IdentityVerificationClient
    payment: PaymentClient
    pg_specific: PgSpecificClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None) -> None:
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._store_id = store_id
        self._client = AsyncClient()

        self.auth = AuthClient(secret=secret, base_url=base_url, store_id=store_id)
        self.platform = PlatformClient(secret=secret, base_url=base_url, store_id=store_id)
        self.identity_verification = IdentityVerificationClient(secret=secret, base_url=base_url, store_id=store_id)
        self.payment = PaymentClient(secret=secret, base_url=base_url, store_id=store_id)
        self.pg_specific = PgSpecificClient(secret=secret, base_url=base_url, store_id=store_id)
