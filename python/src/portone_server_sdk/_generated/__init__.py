from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from urllib.parse import quote
from .auth import AuthClient
from .platform import PlatformClient
from .identity_verification import IdentityVerificationClient
from .payment import PaymentClient
from .pg_specific import PgSpecificClient
from portone_server_sdk._generated import errors
class RootClient:
    _secret: str
    _user_agent: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    auth: AuthClient
    platform: PlatformClient
    identity_verification: IdentityVerificationClient
    payment: PaymentClient
    pg_specific: PgSpecificClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.auth = AuthClient(secret, user_agent, base_url, store_id)
        self.platform = PlatformClient(secret, user_agent, base_url, store_id)
        self.identity_verification = IdentityVerificationClient(secret, user_agent, base_url, store_id)
        self.payment = PaymentClient(secret, user_agent, base_url, store_id)
        self.pg_specific = PgSpecificClient(secret, user_agent, base_url, store_id)
