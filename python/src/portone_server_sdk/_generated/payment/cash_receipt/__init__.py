from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.payment.cash_receipt.cancel_cash_receipt_response import CancelCashReceiptResponse, _deserialize_cancel_cash_receipt_response, _serialize_cancel_cash_receipt_response
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt import CashReceipt, _deserialize_cash_receipt, _serialize_cash_receipt
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_already_issued_error import CashReceiptAlreadyIssuedError, _deserialize_cash_receipt_already_issued_error, _serialize_cash_receipt_already_issued_error
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_not_found_error import CashReceiptNotFoundError, _deserialize_cash_receipt_not_found_error, _serialize_cash_receipt_not_found_error
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_not_issued_error import CashReceiptNotIssuedError, _deserialize_cash_receipt_not_issued_error, _serialize_cash_receipt_not_issued_error
from portone_server_sdk._generated.common.cash_receipt_type import CashReceiptType, _deserialize_cash_receipt_type, _serialize_cash_receipt_type
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.cash_receipt.issue_cash_receipt_customer_input import IssueCashReceiptCustomerInput, _deserialize_issue_cash_receipt_customer_input, _serialize_issue_cash_receipt_customer_input
from portone_server_sdk._generated.payment.cash_receipt.issue_cash_receipt_response import IssueCashReceiptResponse, _deserialize_issue_cash_receipt_response, _serialize_issue_cash_receipt_response
from portone_server_sdk._generated.common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from portone_server_sdk._generated.common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from urllib.parse import quote
from portone_server_sdk._generated import errors
class CashReceiptClient:
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
            CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
                현금영수증이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_NOT_FOUND":
                raise errors.CashReceiptNotFoundError(_deserialize_cash_receipt_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
                현금영수증이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_NOT_FOUND":
                raise errors.CashReceiptNotFoundError(_deserialize_cash_receipt_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cash_receipt(response.json())
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


        Raises:
            CashReceiptAlreadyIssuedError: 현금영수증이 이미 발급된 경우
                현금영수증이 이미 발급된 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/cash-receipts",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_ALREADY_ISSUED":
                raise errors.CashReceiptAlreadyIssuedError(_deserialize_cash_receipt_already_issued_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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


        Raises:
            CashReceiptAlreadyIssuedError: 현금영수증이 이미 발급된 경우
                현금영수증이 이미 발급된 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
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
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/cash-receipts",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_ALREADY_ISSUED":
                raise errors.CashReceiptAlreadyIssuedError(_deserialize_cash_receipt_already_issued_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
                현금영수증이 존재하지 않는 경우
            CashReceiptNotIssuedError: 현금영수증이 발급되지 않은 경우
                현금영수증이 발급되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt/cancel",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_NOT_FOUND":
                raise errors.CashReceiptNotFoundError(_deserialize_cash_receipt_not_found_error(error_response))
            if error_type == "CASH_RECEIPT_NOT_ISSUED":
                raise errors.CashReceiptNotIssuedError(_deserialize_cash_receipt_not_issued_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
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
            CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
                현금영수증이 존재하지 않는 경우
            CashReceiptNotIssuedError: 현금영수증이 발급되지 않은 경우
                현금영수증이 발급되지 않은 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cash-receipt/cancel",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "CASH_RECEIPT_NOT_FOUND":
                raise errors.CashReceiptNotFoundError(_deserialize_cash_receipt_not_found_error(error_response))
            if error_type == "CASH_RECEIPT_NOT_ISSUED":
                raise errors.CashReceiptNotIssuedError(_deserialize_cash_receipt_not_issued_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_cash_receipt_response(response.json())
