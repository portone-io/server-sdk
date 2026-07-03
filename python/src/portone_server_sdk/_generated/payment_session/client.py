from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import ForbiddenError, InvalidRequestError, MaxTtlExceededError, SessionExpiredError, SessionNotFoundError, UnauthorizedError, UnknownError
from ..common.forbidden_error import _deserialize_forbidden_error
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..payment_session.max_ttl_exceeded_error import _deserialize_max_ttl_exceeded_error
from ..payment_session.session_expired_error import _deserialize_session_expired_error
from ..payment_session.session_not_found_error import _deserialize_session_not_found_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..common.checkout_payment_method import CheckoutPaymentMethod, _deserialize_checkout_payment_method, _serialize_checkout_payment_method
from ..payment_session.close_payment_session_response import ClosePaymentSessionResponse, _deserialize_close_payment_session_response, _serialize_close_payment_session_response
from ..common.country import Country, _deserialize_country, _serialize_country
from ..payment_session.create_payment_session_response import CreatePaymentSessionResponse, _deserialize_create_payment_session_response, _serialize_create_payment_session_response
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..payment_session.payment_session import PaymentSession, _deserialize_payment_session, _serialize_payment_session
from ..payment_session.payment_session_agreement import PaymentSessionAgreement, _deserialize_payment_session_agreement, _serialize_payment_session_agreement
from ..payment_session.payment_session_colors import PaymentSessionColors, _deserialize_payment_session_colors, _serialize_payment_session_colors
from ..payment_session.payment_session_product import PaymentSessionProduct, _deserialize_payment_session_product, _serialize_payment_session_product
from urllib.parse import quote
class PaymentSessionClient:
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
    def create_payment_session(
        self,
        *,
        payment_id: str,
        profile_key: str,
        payment_method: Optional[CheckoutPaymentMethod] = None,
        country: Country,
        currency: Currency,
        total_amount: int,
        order_name: str,
        redirect_url: Optional[str] = None,
        products: Optional[list[PaymentSessionProduct]] = None,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        store_name: Optional[str] = None,
        agreements: Optional[list[PaymentSessionAgreement]] = None,
        order_image_url: Optional[str] = None,
        custom_data: Optional[str] = None,
        colors: Optional[PaymentSessionColors] = None,
        ttl_seconds: Optional[int] = None,
    ) -> CreatePaymentSessionResponse:
        """결제 세션 생성

        결제 세션을 생성합니다. 호스티드 체크아웃 페이지가 생성되어 URL이 반환됩니다.

        Args:
            payment_id (str):
                결제 건 아이디
            profile_key (str):
                프로필 키
            payment_method (CheckoutPaymentMethod, optional):
                결제 수단 지정

                지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
            country (Country):
                국가
            currency (Currency):
                통화
            total_amount (int):
                전체 결제 금액
            order_name (str):
                주문명
            redirect_url (str, optional):
                결제 완료 후 리다이렉트 URL

                지정하지 않으면 기본 결과 페이지가 표시됩니다.
            products (list[PaymentSessionProduct], optional):
                주문 항목 목록
            customer_name (str, optional):
                구매자 이름
            customer_email (str, optional):
                구매자 이메일
            store_name (str, optional):
                상점 이름

                페이지 헤더 및 결제사 UI에 표시됩니다.
            agreements (list[PaymentSessionAgreement], optional):
                사용자 지정 약관 목록

                구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
            order_image_url (str, optional):
                주문 대표 이미지 URL
            custom_data (str, optional):
                사용자 지정 데이터

                결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
            colors (PaymentSessionColors, optional):
                체크아웃 페이지 색 설정
            ttl_seconds (int, optional):
                세션 TTL (초)


        Raises:
            CreatePaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["storeId"] = self._store_id
        request_body["paymentId"] = payment_id
        request_body["profileKey"] = profile_key
        if payment_method is not None:
            request_body["paymentMethod"] = _serialize_checkout_payment_method(payment_method)
        request_body["country"] = _serialize_country(country)
        request_body["currency"] = _serialize_currency(currency)
        request_body["totalAmount"] = total_amount
        request_body["orderName"] = order_name
        if redirect_url is not None:
            request_body["redirectUrl"] = redirect_url
        if products is not None:
            request_body["products"] = [_serialize_payment_session_product(item) for item in products]
        if customer_name is not None:
            request_body["customerName"] = customer_name
        if customer_email is not None:
            request_body["customerEmail"] = customer_email
        if store_name is not None:
            request_body["storeName"] = store_name
        if agreements is not None:
            request_body["agreements"] = [_serialize_payment_session_agreement(item) for item in agreements]
        if order_image_url is not None:
            request_body["orderImageUrl"] = order_image_url
        if custom_data is not None:
            request_body["customData"] = custom_data
        if colors is not None:
            request_body["colors"] = _serialize_payment_session_colors(colors)
        if ttl_seconds is not None:
            request_body["ttlSeconds"] = ttl_seconds
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/payment-sessions",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
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
                error = _deserialize_max_ttl_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTtlExceededError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_payment_session_response(response.json())
    async def create_payment_session_async(
        self,
        *,
        payment_id: str,
        profile_key: str,
        payment_method: Optional[CheckoutPaymentMethod] = None,
        country: Country,
        currency: Currency,
        total_amount: int,
        order_name: str,
        redirect_url: Optional[str] = None,
        products: Optional[list[PaymentSessionProduct]] = None,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        store_name: Optional[str] = None,
        agreements: Optional[list[PaymentSessionAgreement]] = None,
        order_image_url: Optional[str] = None,
        custom_data: Optional[str] = None,
        colors: Optional[PaymentSessionColors] = None,
        ttl_seconds: Optional[int] = None,
    ) -> CreatePaymentSessionResponse:
        """결제 세션 생성

        결제 세션을 생성합니다. 호스티드 체크아웃 페이지가 생성되어 URL이 반환됩니다.

        Args:
            payment_id (str):
                결제 건 아이디
            profile_key (str):
                프로필 키
            payment_method (CheckoutPaymentMethod, optional):
                결제 수단 지정

                지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
            country (Country):
                국가
            currency (Currency):
                통화
            total_amount (int):
                전체 결제 금액
            order_name (str):
                주문명
            redirect_url (str, optional):
                결제 완료 후 리다이렉트 URL

                지정하지 않으면 기본 결과 페이지가 표시됩니다.
            products (list[PaymentSessionProduct], optional):
                주문 항목 목록
            customer_name (str, optional):
                구매자 이름
            customer_email (str, optional):
                구매자 이메일
            store_name (str, optional):
                상점 이름

                페이지 헤더 및 결제사 UI에 표시됩니다.
            agreements (list[PaymentSessionAgreement], optional):
                사용자 지정 약관 목록

                구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
            order_image_url (str, optional):
                주문 대표 이미지 URL
            custom_data (str, optional):
                사용자 지정 데이터

                결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
            colors (PaymentSessionColors, optional):
                체크아웃 페이지 색 설정
            ttl_seconds (int, optional):
                세션 TTL (초)


        Raises:
            CreatePaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["storeId"] = self._store_id
        request_body["paymentId"] = payment_id
        request_body["profileKey"] = profile_key
        if payment_method is not None:
            request_body["paymentMethod"] = _serialize_checkout_payment_method(payment_method)
        request_body["country"] = _serialize_country(country)
        request_body["currency"] = _serialize_currency(currency)
        request_body["totalAmount"] = total_amount
        request_body["orderName"] = order_name
        if redirect_url is not None:
            request_body["redirectUrl"] = redirect_url
        if products is not None:
            request_body["products"] = [_serialize_payment_session_product(item) for item in products]
        if customer_name is not None:
            request_body["customerName"] = customer_name
        if customer_email is not None:
            request_body["customerEmail"] = customer_email
        if store_name is not None:
            request_body["storeName"] = store_name
        if agreements is not None:
            request_body["agreements"] = [_serialize_payment_session_agreement(item) for item in agreements]
        if order_image_url is not None:
            request_body["orderImageUrl"] = order_image_url
        if custom_data is not None:
            request_body["customData"] = custom_data
        if colors is not None:
            request_body["colors"] = _serialize_payment_session_colors(colors)
        if ttl_seconds is not None:
            request_body["ttlSeconds"] = ttl_seconds
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/payment-sessions",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": USER_AGENT,
            },
            json=request_body,
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
                error = _deserialize_max_ttl_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTtlExceededError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_payment_session_response(response.json())
    def get_payment_session(
        self,
        *,
        session_id: str,
    ) -> PaymentSession:
        """결제 세션 조회

        결제 세션을 조회합니다. 인증 헤더 없이 웹 페이지에서도 접근 가능합니다.

        Args:
            session_id (str):
                결제 세션 아이디


        Raises:
            GetPaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/payment-sessions/{quote(session_id, safe='')}",
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
                error = _deserialize_session_expired_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionExpiredError(error)
            try:
                error = _deserialize_session_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionNotFoundError(error)
            raise UnknownError(error_response)
        return _deserialize_payment_session(response.json())
    async def get_payment_session_async(
        self,
        *,
        session_id: str,
    ) -> PaymentSession:
        """결제 세션 조회

        결제 세션을 조회합니다. 인증 헤더 없이 웹 페이지에서도 접근 가능합니다.

        Args:
            session_id (str):
                결제 세션 아이디


        Raises:
            GetPaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/payment-sessions/{quote(session_id, safe='')}",
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
                error = _deserialize_session_expired_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionExpiredError(error)
            try:
                error = _deserialize_session_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionNotFoundError(error)
            raise UnknownError(error_response)
        return _deserialize_payment_session(response.json())
    def close_payment_session(
        self,
        *,
        session_id: str,
    ) -> ClosePaymentSessionResponse:
        """결제 세션 종료

        결제 세션을 즉시 만료시킵니다. 이후 해당 세션으로는 결제 페이지에 접근할 수 없습니다.

        Args:
            session_id (str):
                결제 세션 아이디


        Raises:
            ClosePaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/payment-sessions/{quote(session_id, safe='')}/close",
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
                error = _deserialize_session_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_close_payment_session_response(response.json())
    async def close_payment_session_async(
        self,
        *,
        session_id: str,
    ) -> ClosePaymentSessionResponse:
        """결제 세션 종료

        결제 세션을 즉시 만료시킵니다. 이후 해당 세션으로는 결제 페이지에 접근할 수 없습니다.

        Args:
            session_id (str):
                결제 세션 아이디


        Raises:
            ClosePaymentSessionError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/payment-sessions/{quote(session_id, safe='')}/close",
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
                error = _deserialize_session_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SessionNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_close_payment_session_response(response.json())
