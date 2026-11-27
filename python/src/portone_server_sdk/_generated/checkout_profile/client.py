from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import InvalidRequestError, ProfileSettingsNotFoundError, UnknownError
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..checkout_profile.profile_settings_not_found_error import _deserialize_profile_settings_not_found_error
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..checkout_profile.evaluate_checkout_profile_response import EvaluateCheckoutProfileResponse, _deserialize_evaluate_checkout_profile_response, _serialize_evaluate_checkout_profile_response
from urllib.parse import quote
class CheckoutProfileClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _async_client: AsyncClient
    _sync_client: SyncClient

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
    def evaluate_checkout_profile(
        self,
        *,
        profile_key: str,
        country: Country,
        currency: Currency,
        amount: int,
    ) -> EvaluateCheckoutProfileResponse:
        """체크아웃 프로필에서 결제 수단 목록 조회

        주어진 금액 및 국가에서 사용 가능한 결제 수단 목록을 반환

        Args:
            profile_key (str):
                프로필 키
            country (Country):
                국가
            currency (Currency):
                통화
            amount (int):
                결제 금액
                (int64)


        Raises:
            EvaluateCheckoutProfileError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if profile_key is not None:
            query.append(("profileKey", profile_key))
        if country is not None:
            query.append(("country", country))
        if currency is not None:
            query.append(("currency", currency))
        if amount is not None:
            query.append(("amount", amount))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/checkout-profiles/evaluate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_profile_settings_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ProfileSettingsNotFoundError(error)
            raise UnknownError(error_response)
        return _deserialize_evaluate_checkout_profile_response(response.json())
    async def evaluate_checkout_profile_async(
        self,
        *,
        profile_key: str,
        country: Country,
        currency: Currency,
        amount: int,
    ) -> EvaluateCheckoutProfileResponse:
        """체크아웃 프로필에서 결제 수단 목록 조회

        주어진 금액 및 국가에서 사용 가능한 결제 수단 목록을 반환

        Args:
            profile_key (str):
                프로필 키
            country (Country):
                국가
            currency (Currency):
                통화
            amount (int):
                결제 금액
                (int64)


        Raises:
            EvaluateCheckoutProfileError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if profile_key is not None:
            query.append(("profileKey", profile_key))
        if country is not None:
            query.append(("country", country))
        if currency is not None:
            query.append(("currency", currency))
        if amount is not None:
            query.append(("amount", amount))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/checkout-profiles/evaluate",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_profile_settings_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ProfileSettingsNotFoundError(error)
            raise UnknownError(error_response)
        return _deserialize_evaluate_checkout_profile_response(response.json())
