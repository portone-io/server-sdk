from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ChannelNotFoundError, InvalidRequestError, PgProviderError, UnauthorizedError, UnknownError
from ...common.channel_not_found_error import _deserialize_channel_not_found_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.pg_provider_error import _deserialize_pg_provider_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...payment.additional_feature.get_pg_card_promotions_response import GetPgCardPromotionsResponse, _deserialize_get_pg_card_promotions_response, _serialize_get_pg_card_promotions_response
from ...payment.additional_feature.pg_promotion_card_company import PgPromotionCardCompany, _deserialize_pg_promotion_card_company, _serialize_pg_promotion_card_company
from urllib.parse import quote
class AdditionalFeatureClient:
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
    def get_pg_card_promotions(
        self,
        *,
        channel_key: str,
        amount: int,
        card_company: Optional[PgPromotionCardCompany] = None,
    ) -> GetPgCardPromotionsResponse:
        """PG사 카드 프로모션 조회 API

        주어진 채널에 대해 PG사에서 제공하는 카드 프로모션 목록을 조회합니다.
        해당 API는 현재 특정 PG사(KCP_V2)에 대해서만 지원되며, 지원 여부는 포트원 기술지원팀에 문의 부탁드립니다.

        Args:
            channel_key (str):
                채널 키

                조회하고자 하는 채널의 키
            amount (int):
                결제 금액

                결제 금액입니다. 해당 결제 금액 기준 이용 가능한 프로모션 목록이 조회됩니다.
                (int64)
            card_company (PgPromotionCardCompany, optional):
                카드사 필터

                조회할 카드사입니다. 값을 입력하지 않으면 카드사 필터링이 적용되지 않습니다.


        Raises:
            GetPgCardPromotionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if channel_key is not None:
            query.append(("channelKey", channel_key))
        if amount is not None:
            query.append(("amount", amount))
        if card_company is not None:
            query.append(("cardCompany", card_company))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/payment-gateways/card-promotion",
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
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_pg_card_promotions_response(response.json())
    async def get_pg_card_promotions_async(
        self,
        *,
        channel_key: str,
        amount: int,
        card_company: Optional[PgPromotionCardCompany] = None,
    ) -> GetPgCardPromotionsResponse:
        """PG사 카드 프로모션 조회 API

        주어진 채널에 대해 PG사에서 제공하는 카드 프로모션 목록을 조회합니다.
        해당 API는 현재 특정 PG사(KCP_V2)에 대해서만 지원되며, 지원 여부는 포트원 기술지원팀에 문의 부탁드립니다.

        Args:
            channel_key (str):
                채널 키

                조회하고자 하는 채널의 키
            amount (int):
                결제 금액

                결제 금액입니다. 해당 결제 금액 기준 이용 가능한 프로모션 목록이 조회됩니다.
                (int64)
            card_company (PgPromotionCardCompany, optional):
                카드사 필터

                조회할 카드사입니다. 값을 입력하지 않으면 카드사 필터링이 적용되지 않습니다.


        Raises:
            GetPgCardPromotionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if channel_key is not None:
            query.append(("channelKey", channel_key))
        if amount is not None:
            query.append(("amount", amount))
        if card_company is not None:
            query.append(("cardCompany", card_company))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/payment-gateways/card-promotion",
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
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_pg_card_promotions_response(response.json())
