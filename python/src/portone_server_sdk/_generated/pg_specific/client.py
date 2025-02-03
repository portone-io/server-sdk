from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import InvalidRequestError, UnauthorizedError, UnknownError
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..pg_specific.get_kakaopay_payment_order_response import GetKakaopayPaymentOrderResponse, _deserialize_get_kakaopay_payment_order_response, _serialize_get_kakaopay_payment_order_response
from urllib.parse import quote
class PgSpecificClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
    def get_kakaopay_payment_order(
        self,
        *,
        pg_tx_id: str,
        channel_key: str,
    ) -> GetKakaopayPaymentOrderResponse:
        """카카오페이 주문 조회 API

        주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
        해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.

        Args:
            pg_tx_id (str):
                카카오페이 주문 번호 (tid)
            channel_key (str):
                채널 키


        Raises:
            GetKakaopayPaymentOrderError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if pg_tx_id is not None:
            query.append(("pgTxId", pg_tx_id))
        if channel_key is not None:
            query.append(("channelKey", channel_key))
        response = httpx.request(
            "GET",
            f"{self._base_url}/kakaopay/payment/order",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_kakaopay_payment_order_response(response.json())
    async def get_kakaopay_payment_order_async(
        self,
        *,
        pg_tx_id: str,
        channel_key: str,
    ) -> GetKakaopayPaymentOrderResponse:
        """카카오페이 주문 조회 API

        주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
        해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.

        Args:
            pg_tx_id (str):
                카카오페이 주문 번호 (tid)
            channel_key (str):
                채널 키


        Raises:
            GetKakaopayPaymentOrderError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if pg_tx_id is not None:
            query.append(("pgTxId", pg_tx_id))
        if channel_key is not None:
            query.append(("channelKey", channel_key))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/kakaopay/payment/order",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_kakaopay_payment_order_response(response.json())
