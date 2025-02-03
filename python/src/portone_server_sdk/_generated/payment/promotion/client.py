from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PromotionNotFoundError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...payment.promotion.promotion_not_found_error import _deserialize_promotion_not_found_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...payment.promotion.promotion import Promotion, _deserialize_promotion, _serialize_promotion
from urllib.parse import quote
class PromotionClient:
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
    def get_promotion(
        self,
        *,
        promotion_id: str,
    ) -> Promotion:
        """프로모션 단건 조회

        주어진 아이디에 대응되는 프로모션을 조회합니다.

        Args:
            promotion_id (str):
                조회할 프로모션 아이디


        Raises:
            GetPromotionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/promotions/{quote(promotion_id, safe='')}",
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
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_promotion_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_promotion(response.json())
    async def get_promotion_async(
        self,
        *,
        promotion_id: str,
    ) -> Promotion:
        """프로모션 단건 조회

        주어진 아이디에 대응되는 프로모션을 조회합니다.

        Args:
            promotion_id (str):
                조회할 프로모션 아이디


        Raises:
            GetPromotionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/promotions/{quote(promotion_id, safe='')}",
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
                error = _deserialize_forbidden_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ForbiddenError(error)
            try:
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_promotion_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_promotion(response.json())
