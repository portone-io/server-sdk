from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from urllib.parse import quote
from .tax_invoice.client import TaxInvoiceClient
class B2bClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _async_client: AsyncClient
    _sync_client: SyncClient
    tax_invoice: TaxInvoiceClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """
        API Secret을 사용해 포트원 API 클라이언트를 생성합니다.

        Args:
            secret (str): 포트원 API Secret입니다.
            base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 `"https://api.portone.io"`입니다.
            store_id: 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
            """
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._async_client = AsyncClient(timeout=60.0)
        self._sync_client = SyncClient(timeout=60.0)
        self.tax_invoice = TaxInvoiceClient(secret=secret, base_url=base_url, store_id=store_id)
