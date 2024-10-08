from __future__ import annotations
from typing import Optional
from httpx import AsyncClient
from .auth import AuthClient
from .platform import PlatformClient
from .identity_verification import IdentityVerificationClient
from .payment import PaymentClient
from .billing_key import BillingKeyClient
from .cash_receipt import CashReceiptClient
from .payment_schedule import PaymentScheduleClient
from .analytics import AnalyticsClient
from .b2b import B2BClient
from .pg_specific import PgSpecificClient
from .promotion import PromotionClient

class PortOneClient:
    _secret: str
    _store_id: Optional[str]
    _base_url: str
    _user_agent: str
    _client: AsyncClient
    auth: AuthClient
    platform: PlatformClient
    identity_verification: IdentityVerificationClient
    payment: PaymentClient
    billing_key: BillingKeyClient
    cash_receipt: CashReceiptClient
    payment_schedule: PaymentScheduleClient
    analytics: AnalyticsClient
    b2b: B2BClient
    pg_specific: PgSpecificClient
    promotion: PromotionClient

    def __init__(self, *, secret: str, store_id: Optional[str] = None, base_url: str = "https://api.portone.io") -> None:
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
        """
        self._secret = secret
        self._store_id = store_id
        self._client = AsyncClient()
        user_agent = "__USER_AGENT__"

        self.auth = AuthClient(secret, user_agent, base_url, store_id)
        self.platform = PlatformClient(secret, user_agent, base_url, store_id)
        self.identity_verification = IdentityVerificationClient(secret, user_agent, base_url, store_id)
        self.payment = PaymentClient(secret, user_agent, base_url, store_id)
        self.billing_key = BillingKeyClient(secret, user_agent, base_url, store_id)
        self.cash_receipt = CashReceiptClient(secret, user_agent, base_url, store_id)
        self.payment_schedule = PaymentScheduleClient(secret, user_agent, base_url, store_id)
        self.analytics = AnalyticsClient(secret, user_agent, base_url, store_id)
        self.b2b = B2BClient(secret, user_agent, base_url, store_id)
        self.pg_specific = PgSpecificClient(secret, user_agent, base_url, store_id)
        self.promotion = PromotionClient(secret, user_agent, base_url, store_id)
