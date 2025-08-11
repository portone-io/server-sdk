from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import CashReceiptAlreadyIssuedError, CashReceiptNotFoundError, CashReceiptNotIssuedError, ChannelNotFoundError, ForbiddenError, InvalidRequestError, PgProviderError, UnauthorizedError, UnknownError
from ...payment.cash_receipt.cash_receipt_already_issued_error import _deserialize_cash_receipt_already_issued_error
from ...payment.cash_receipt.cash_receipt_not_found_error import _deserialize_cash_receipt_not_found_error
from ...payment.cash_receipt.cash_receipt_not_issued_error import _deserialize_cash_receipt_not_issued_error
from ...common.channel_not_found_error import _deserialize_channel_not_found_error
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...common.pg_provider_error import _deserialize_pg_provider_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...payment.cash_receipt.cancel_cash_receipt_response import CancelCashReceiptResponse, _deserialize_cancel_cash_receipt_response, _serialize_cancel_cash_receipt_response
from ...payment.cash_receipt.cash_receipt import CashReceipt, _deserialize_cash_receipt, _serialize_cash_receipt
from ...payment.cash_receipt.cash_receipt_filter_input import CashReceiptFilterInput, _deserialize_cash_receipt_filter_input, _serialize_cash_receipt_filter_input
from ...payment.cash_receipt.cash_receipt_sort_input import CashReceiptSortInput, _deserialize_cash_receipt_sort_input, _serialize_cash_receipt_sort_input
from ...common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from ...common.currency import Currency, _deserialize_currency, _serialize_currency
from ...payment.cash_receipt.get_cash_receipts_response import GetCashReceiptsResponse, _deserialize_get_cash_receipts_response, _serialize_get_cash_receipts_response
from ...payment.cash_receipt.issue_cash_receipt_customer_input import IssueCashReceiptCustomerInput, _deserialize_issue_cash_receipt_customer_input, _serialize_issue_cash_receipt_customer_input
from ...payment.cash_receipt.issue_cash_receipt_payment_method_type import IssueCashReceiptPaymentMethodType, _deserialize_issue_cash_receipt_payment_method_type, _serialize_issue_cash_receipt_payment_method_type
from ...payment.cash_receipt.issue_cash_receipt_response import IssueCashReceiptResponse, _deserialize_issue_cash_receipt_response, _serialize_issue_cash_receipt_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from ...common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from urllib.parse import quote
class CashReceiptClient:
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
    def get_cash_receipts(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[CashReceiptSortInput] = None,
        filter: Optional[CashReceiptFilterInput] = None,
    ) -> GetCashReceiptsResponse:
        """현금영수증 다건 조회

        주어진 조건에 맞는 현금영수증들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (CashReceiptSortInput, optional):
                정렬 조건

                미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (CashReceiptFilterInput, optional):
                조회할 현금영수증 조건 필터


        Raises:
            GetCashReceiptsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_cash_receipt_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_cash_receipt_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/cash-receipts",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_cash_receipts_response(response.json())
    async def get_cash_receipts_async(
        self,
        *,
        page: Optional[PageInput] = None,
        sort: Optional[CashReceiptSortInput] = None,
        filter: Optional[CashReceiptFilterInput] = None,
    ) -> GetCashReceiptsResponse:
        """현금영수증 다건 조회

        주어진 조건에 맞는 현금영수증들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (CashReceiptSortInput, optional):
                정렬 조건

                미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (CashReceiptFilterInput, optional):
                조회할 현금영수증 조건 필터


        Raises:
            GetCashReceiptsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if sort is not None:
            request_body["sort"] = _serialize_cash_receipt_sort_input(sort)
        if filter is not None:
            request_body["filter"] = _serialize_cash_receipt_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/cash-receipts",
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_cash_receipts_response(response.json())
    def issue_cash_receipt(
        self,
        *,
        payment_id: str,
        channel_key: str,
        type: CashReceiptType,
        order_name: str,
        currency: Currency,
        amount: PaymentAmountInput,
        product_type: Optional[PaymentProductType] = None,
        customer: IssueCashReceiptCustomerInput,
        paid_at: Optional[str] = None,
        business_registration_number: Optional[str] = None,
        payment_method: Optional[IssueCashReceiptPaymentMethodType] = None,
    ) -> IssueCashReceiptResponse:
        """현금 영수증 수동 발급

        현금 영수증 발급을 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디

                외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
            channel_key (str):
                채널 키
            type (CashReceiptType):
                현금 영수증 유형
            order_name (str):
                주문명
            currency (Currency):
                화폐
            amount (PaymentAmountInput):
                금액 세부 입력 정보
            product_type (PaymentProductType, optional):
                상품 유형
            customer (IssueCashReceiptCustomerInput):
                고객 정보
            paid_at (str, optional):
                결제 일자
            business_registration_number (str, optional):
                사업자등록번호

                웰컴페이먼츠의 경우에만 입력합니다.
            payment_method (IssueCashReceiptPaymentMethodType, optional):
                결제 수단

                웰컴페이먼츠의 경우에만 입력합니다.


        Raises:
            IssueCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["paymentId"] = payment_id
        request_body["channelKey"] = channel_key
        request_body["type"] = _serialize_cash_receipt_type(type)
        request_body["orderName"] = order_name
        request_body["currency"] = _serialize_currency(currency)
        request_body["amount"] = _serialize_payment_amount_input(amount)
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        request_body["customer"] = _serialize_issue_cash_receipt_customer_input(customer)
        if paid_at is not None:
            request_body["paidAt"] = paid_at
        if business_registration_number is not None:
            request_body["businessRegistrationNumber"] = business_registration_number
        if payment_method is not None:
            request_body["paymentMethod"] = _serialize_issue_cash_receipt_payment_method_type(payment_method)
        query = []
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/cash-receipts",
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
                error = _deserialize_cash_receipt_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptAlreadyIssuedError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
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
        return _deserialize_issue_cash_receipt_response(response.json())
    async def issue_cash_receipt_async(
        self,
        *,
        payment_id: str,
        channel_key: str,
        type: CashReceiptType,
        order_name: str,
        currency: Currency,
        amount: PaymentAmountInput,
        product_type: Optional[PaymentProductType] = None,
        customer: IssueCashReceiptCustomerInput,
        paid_at: Optional[str] = None,
        business_registration_number: Optional[str] = None,
        payment_method: Optional[IssueCashReceiptPaymentMethodType] = None,
    ) -> IssueCashReceiptResponse:
        """현금 영수증 수동 발급

        현금 영수증 발급을 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디

                외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
            channel_key (str):
                채널 키
            type (CashReceiptType):
                현금 영수증 유형
            order_name (str):
                주문명
            currency (Currency):
                화폐
            amount (PaymentAmountInput):
                금액 세부 입력 정보
            product_type (PaymentProductType, optional):
                상품 유형
            customer (IssueCashReceiptCustomerInput):
                고객 정보
            paid_at (str, optional):
                결제 일자
            business_registration_number (str, optional):
                사업자등록번호

                웰컴페이먼츠의 경우에만 입력합니다.
            payment_method (IssueCashReceiptPaymentMethodType, optional):
                결제 수단

                웰컴페이먼츠의 경우에만 입력합니다.


        Raises:
            IssueCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["paymentId"] = payment_id
        request_body["channelKey"] = channel_key
        request_body["type"] = _serialize_cash_receipt_type(type)
        request_body["orderName"] = order_name
        request_body["currency"] = _serialize_currency(currency)
        request_body["amount"] = _serialize_payment_amount_input(amount)
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        request_body["customer"] = _serialize_issue_cash_receipt_customer_input(customer)
        if paid_at is not None:
            request_body["paidAt"] = paid_at
        if business_registration_number is not None:
            request_body["businessRegistrationNumber"] = business_registration_number
        if payment_method is not None:
            request_body["paymentMethod"] = _serialize_issue_cash_receipt_payment_method_type(payment_method)
        query = []
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/cash-receipts",
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
                error = _deserialize_cash_receipt_already_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptAlreadyIssuedError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
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
        return _deserialize_issue_cash_receipt_response(response.json())
    def cancel_cash_receipt_by_payment_id(
        self,
        *,
        payment_id: str,
    ) -> CancelCashReceiptResponse:
        """현금 영수증 취소

        현금 영수증 취소를 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            CancelCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = self._sync_client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt/cancel",
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
                error = _deserialize_cash_receipt_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotFoundError(error)
            try:
                error = _deserialize_cash_receipt_not_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotIssuedError(error)
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
        return _deserialize_cancel_cash_receipt_response(response.json())
    async def cancel_cash_receipt_by_payment_id_async(
        self,
        *,
        payment_id: str,
    ) -> CancelCashReceiptResponse:
        """현금 영수증 취소

        현금 영수증 취소를 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            CancelCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._async_client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt/cancel",
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
                error = _deserialize_cash_receipt_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotFoundError(error)
            try:
                error = _deserialize_cash_receipt_not_issued_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotIssuedError(error)
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
        return _deserialize_cancel_cash_receipt_response(response.json())
    def get_cash_receipt_by_payment_id(
        self,
        *,
        payment_id: str,
    ) -> CashReceipt:
        """현금 영수증 단건 조회

        주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            GetCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt",
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
                error = _deserialize_cash_receipt_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotFoundError(error)
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cash_receipt(response.json())
    async def get_cash_receipt_by_payment_id_async(
        self,
        *,
        payment_id: str,
    ) -> CashReceipt:
        """현금 영수증 단건 조회

        주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            GetCashReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt",
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
                error = _deserialize_cash_receipt_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CashReceiptNotFoundError(error)
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
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_cash_receipt(response.json())
