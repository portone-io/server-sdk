from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import InvalidRequestError, PaymentNotFoundError, UnauthorizedError, UnknownError
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.payment_not_found_error import _deserialize_payment_not_found_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..pg_specific.confirm_paymentwall_delivery_response import ConfirmPaymentwallDeliveryResponse, _deserialize_confirm_paymentwall_delivery_response, _serialize_confirm_paymentwall_delivery_response
from ..common.country import Country, _deserialize_country, _serialize_country
from ..pg_specific.get_kakaopay_payment_order_response import GetKakaopayPaymentOrderResponse, _deserialize_get_kakaopay_payment_order_response, _serialize_get_kakaopay_payment_order_response
from ..pg_specific.paymentwall_delivery_status import PaymentwallDeliveryStatus, _deserialize_paymentwall_delivery_status, _serialize_paymentwall_delivery_status
from ..pg_specific.paymentwall_delivery_type import PaymentwallDeliveryType, _deserialize_paymentwall_delivery_type, _serialize_paymentwall_delivery_type
from urllib.parse import quote
class PgSpecificClient:
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
        response = self._sync_client.request(
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
        response = await self._async_client.request(
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
    def confirm_paymentwall_delivery(
        self,
        *,
        transaction_id: str,
        delivery_type: PaymentwallDeliveryType,
        delivery_status: PaymentwallDeliveryStatus,
        estimated_delivery_datetime: str,
        estimated_update_datetime: str,
        reason: Optional[str] = None,
        refundable: bool,
        details: str,
        shipping_address_email: str,
        carrier_tracking_id: Optional[str] = None,
        carrier_type: Optional[str] = None,
        shipping_address_country: Optional[Country] = None,
        shipping_address_city: Optional[str] = None,
        shipping_address_zip: Optional[str] = None,
        shipping_address_state: Optional[str] = None,
        shipping_address_street: Optional[str] = None,
        shipping_address_phone: Optional[str] = None,
        shipping_address_firstname: Optional[str] = None,
        shipping_address_lastname: Optional[str] = None,
        attachments: Optional[list[str]] = None,
    ) -> ConfirmPaymentwallDeliveryResponse:
        """페이먼트월 배송 정보 등록

        배송 정보를 페이먼트월에 등록합니다.
        등록된 배송 정보는 차지백 발생 시 고객사의 상품 배송 완료 증빙 자료로 활용되므로, 반드시 연동해야 합니다.

        Args:
            transaction_id (str):
                결제 건 포트원 채번 아이디
            delivery_type (PaymentwallDeliveryType):
                배송 유형
            delivery_status (PaymentwallDeliveryStatus):
                배송 상태
            estimated_delivery_datetime (str):
                배송 완료 예상 일시

                배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
                (RFC 3339 date-time)
            estimated_update_datetime (str):
                배송 상태 업데이트 예정 일시

                배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
                (RFC 3339 date-time)
            reason (str, optional):
                상태 변경 사유
            refundable (bool):
                환불 가능 여부
            details (str):
                상세 설명
            shipping_address_email (str):
                고객 이메일 주소
            carrier_tracking_id (str, optional):
                운송장 번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            carrier_type (str, optional):
                운송사 이름

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_country (Country, optional):
                수신자 국가

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_city (str, optional):
                수신자 도시

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_zip (str, optional):
                수신자 우편번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_state (str, optional):
                수신자 주

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_street (str, optional):
                수신자 도로명 주소

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_phone (str, optional):
                수신자 전화번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_firstname (str, optional):
                수신자 이름

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_lastname (str, optional):
                수신자 성

                배송 유형이 PHYSICAL인 경우 필수입니다.
            attachments (list[str], optional):
                배송 증빙 첨부 파일 URL 목록

                배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.


        Raises:
            ConfirmPaymentwallDeliveryError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["transactionId"] = transaction_id
        request_body["deliveryType"] = _serialize_paymentwall_delivery_type(delivery_type)
        request_body["deliveryStatus"] = _serialize_paymentwall_delivery_status(delivery_status)
        request_body["estimatedDeliveryDatetime"] = estimated_delivery_datetime
        request_body["estimatedUpdateDatetime"] = estimated_update_datetime
        if reason is not None:
            request_body["reason"] = reason
        request_body["refundable"] = refundable
        request_body["details"] = details
        request_body["shippingAddressEmail"] = shipping_address_email
        if carrier_tracking_id is not None:
            request_body["carrierTrackingId"] = carrier_tracking_id
        if carrier_type is not None:
            request_body["carrierType"] = carrier_type
        if shipping_address_country is not None:
            request_body["shippingAddressCountry"] = _serialize_country(shipping_address_country)
        if shipping_address_city is not None:
            request_body["shippingAddressCity"] = shipping_address_city
        if shipping_address_zip is not None:
            request_body["shippingAddressZip"] = shipping_address_zip
        if shipping_address_state is not None:
            request_body["shippingAddressState"] = shipping_address_state
        if shipping_address_street is not None:
            request_body["shippingAddressStreet"] = shipping_address_street
        if shipping_address_phone is not None:
            request_body["shippingAddressPhone"] = shipping_address_phone
        if shipping_address_firstname is not None:
            request_body["shippingAddressFirstname"] = shipping_address_firstname
        if shipping_address_lastname is not None:
            request_body["shippingAddressLastname"] = shipping_address_lastname
        if attachments is not None:
            request_body["attachments"] = attachments
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/paymentwall/delivery/confirm",
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirm_paymentwall_delivery_response(response.json())
    async def confirm_paymentwall_delivery_async(
        self,
        *,
        transaction_id: str,
        delivery_type: PaymentwallDeliveryType,
        delivery_status: PaymentwallDeliveryStatus,
        estimated_delivery_datetime: str,
        estimated_update_datetime: str,
        reason: Optional[str] = None,
        refundable: bool,
        details: str,
        shipping_address_email: str,
        carrier_tracking_id: Optional[str] = None,
        carrier_type: Optional[str] = None,
        shipping_address_country: Optional[Country] = None,
        shipping_address_city: Optional[str] = None,
        shipping_address_zip: Optional[str] = None,
        shipping_address_state: Optional[str] = None,
        shipping_address_street: Optional[str] = None,
        shipping_address_phone: Optional[str] = None,
        shipping_address_firstname: Optional[str] = None,
        shipping_address_lastname: Optional[str] = None,
        attachments: Optional[list[str]] = None,
    ) -> ConfirmPaymentwallDeliveryResponse:
        """페이먼트월 배송 정보 등록

        배송 정보를 페이먼트월에 등록합니다.
        등록된 배송 정보는 차지백 발생 시 고객사의 상품 배송 완료 증빙 자료로 활용되므로, 반드시 연동해야 합니다.

        Args:
            transaction_id (str):
                결제 건 포트원 채번 아이디
            delivery_type (PaymentwallDeliveryType):
                배송 유형
            delivery_status (PaymentwallDeliveryStatus):
                배송 상태
            estimated_delivery_datetime (str):
                배송 완료 예상 일시

                배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
                (RFC 3339 date-time)
            estimated_update_datetime (str):
                배송 상태 업데이트 예정 일시

                배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
                (RFC 3339 date-time)
            reason (str, optional):
                상태 변경 사유
            refundable (bool):
                환불 가능 여부
            details (str):
                상세 설명
            shipping_address_email (str):
                고객 이메일 주소
            carrier_tracking_id (str, optional):
                운송장 번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            carrier_type (str, optional):
                운송사 이름

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_country (Country, optional):
                수신자 국가

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_city (str, optional):
                수신자 도시

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_zip (str, optional):
                수신자 우편번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_state (str, optional):
                수신자 주

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_street (str, optional):
                수신자 도로명 주소

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_phone (str, optional):
                수신자 전화번호

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_firstname (str, optional):
                수신자 이름

                배송 유형이 PHYSICAL인 경우 필수입니다.
            shipping_address_lastname (str, optional):
                수신자 성

                배송 유형이 PHYSICAL인 경우 필수입니다.
            attachments (list[str], optional):
                배송 증빙 첨부 파일 URL 목록

                배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.


        Raises:
            ConfirmPaymentwallDeliveryError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["transactionId"] = transaction_id
        request_body["deliveryType"] = _serialize_paymentwall_delivery_type(delivery_type)
        request_body["deliveryStatus"] = _serialize_paymentwall_delivery_status(delivery_status)
        request_body["estimatedDeliveryDatetime"] = estimated_delivery_datetime
        request_body["estimatedUpdateDatetime"] = estimated_update_datetime
        if reason is not None:
            request_body["reason"] = reason
        request_body["refundable"] = refundable
        request_body["details"] = details
        request_body["shippingAddressEmail"] = shipping_address_email
        if carrier_tracking_id is not None:
            request_body["carrierTrackingId"] = carrier_tracking_id
        if carrier_type is not None:
            request_body["carrierType"] = carrier_type
        if shipping_address_country is not None:
            request_body["shippingAddressCountry"] = _serialize_country(shipping_address_country)
        if shipping_address_city is not None:
            request_body["shippingAddressCity"] = shipping_address_city
        if shipping_address_zip is not None:
            request_body["shippingAddressZip"] = shipping_address_zip
        if shipping_address_state is not None:
            request_body["shippingAddressState"] = shipping_address_state
        if shipping_address_street is not None:
            request_body["shippingAddressStreet"] = shipping_address_street
        if shipping_address_phone is not None:
            request_body["shippingAddressPhone"] = shipping_address_phone
        if shipping_address_firstname is not None:
            request_body["shippingAddressFirstname"] = shipping_address_firstname
        if shipping_address_lastname is not None:
            request_body["shippingAddressLastname"] = shipping_address_lastname
        if attachments is not None:
            request_body["attachments"] = attachments
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/paymentwall/delivery/confirm",
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
                error = _deserialize_invalid_request_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise InvalidRequestError(error)
            try:
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_confirm_paymentwall_delivery_response(response.json())
