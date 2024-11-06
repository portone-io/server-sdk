from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.pg_specific.get_kakaopay_payment_order_response import GetKakaopayPaymentOrderResponse, _deserialize_get_kakaopay_payment_order_response, _serialize_get_kakaopay_payment_order_response
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class PgSpecificClient:
    _secret: str
    _user_agent: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_kakaopay_payment_order_response(response.json())
