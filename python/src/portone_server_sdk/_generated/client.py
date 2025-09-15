from __future__ import annotations
from typing import Optional
from .b2b.client import B2bClient
from .platform.client import PlatformClient
from .payment.client import PaymentClient
from .identity_verification.client import IdentityVerificationClient
from .pg_specific.client import PgSpecificClient
from .auth.client import AuthClient

class PortOneClient:
    b2b: B2bClient
    platform: PlatformClient
    payment: PaymentClient
    identity_verification: IdentityVerificationClient
    pg_specific: PgSpecificClient
    auth: AuthClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None) -> None:
        """
        API Secret을 사용해 포트원 API 클라이언트를 생성합니다.

        Args:
            secret (str): 포트원 API Secret입니다.")
            base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
            store_id (str, optional): 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
        """

        self.b2b = B2bClient(secret=secret, base_url=base_url, store_id=store_id)
        self.platform = PlatformClient(secret=secret, base_url=base_url, store_id=store_id)
        self.payment = PaymentClient(secret=secret, base_url=base_url, store_id=store_id)
        self.identity_verification = IdentityVerificationClient(secret=secret, base_url=base_url, store_id=store_id)
        self.pg_specific = PgSpecificClient(secret=secret, base_url=base_url, store_id=store_id)
        self.auth = AuthClient(secret=secret, base_url=base_url, store_id=store_id)
