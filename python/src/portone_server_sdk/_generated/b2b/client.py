from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from urllib.parse import quote
from .business.client import BusinessClient
class B2BClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    business: BusinessClient

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
        self._client = AsyncClient()
        self.business = BusinessClient(secret=secret, base_url=base_url, store_id=store_id)
