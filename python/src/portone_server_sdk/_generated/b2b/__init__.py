from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from .member_company import MemberCompanyClient
from .contact import ContactClient
from .tax_invoice import TaxInvoiceClient
from portone_server_sdk._generated import errors
class B2BClient:
    _secret: str
    _user_agent: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    member_company: MemberCompanyClient
    contact: ContactClient
    tax_invoice: TaxInvoiceClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.member_company = MemberCompanyClient(secret, user_agent, base_url, store_id)
        self.contact = ContactClient(secret, user_agent, base_url, store_id)
        self.tax_invoice = TaxInvoiceClient(secret, user_agent, base_url, store_id)
