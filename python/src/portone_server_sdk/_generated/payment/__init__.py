from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.payment.already_paid_error import AlreadyPaidError, _deserialize_already_paid_error, _serialize_already_paid_error
from portone_server_sdk._generated.payment.apply_escrow_logistics_response import ApplyEscrowLogisticsResponse, _deserialize_apply_escrow_logistics_response, _serialize_apply_escrow_logistics_response
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.payment.cancel_amount_exceeds_cancellable_amount_error import CancelAmountExceedsCancellableAmountError, _deserialize_cancel_amount_exceeds_cancellable_amount_error, _serialize_cancel_amount_exceeds_cancellable_amount_error
from portone_server_sdk._generated.payment.cancel_payment_body_refund_account import CancelPaymentBodyRefundAccount, _deserialize_cancel_payment_body_refund_account, _serialize_cancel_payment_body_refund_account
from portone_server_sdk._generated.payment.cancel_payment_response import CancelPaymentResponse, _deserialize_cancel_payment_response, _serialize_cancel_payment_response
from portone_server_sdk._generated.payment.cancel_requester import CancelRequester, _deserialize_cancel_requester, _serialize_cancel_requester
from portone_server_sdk._generated.payment.cancel_tax_amount_exceeds_cancellable_tax_amount_error import CancelTaxAmountExceedsCancellableTaxAmountError, _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error, _serialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error
from portone_server_sdk._generated.payment.cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError, _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error, _serialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error
from portone_server_sdk._generated.payment.cancellable_amount_consistency_broken_error import CancellableAmountConsistencyBrokenError, _deserialize_cancellable_amount_consistency_broken_error, _serialize_cancellable_amount_consistency_broken_error
from portone_server_sdk._generated.common.cash_receipt_input import CashReceiptInput, _deserialize_cash_receipt_input, _serialize_cash_receipt_input
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.payment.close_virtual_account_response import CloseVirtualAccountResponse, _deserialize_close_virtual_account_response, _serialize_close_virtual_account_response
from portone_server_sdk._generated.payment.confirm_escrow_response import ConfirmEscrowResponse, _deserialize_confirm_escrow_response, _serialize_confirm_escrow_response
from portone_server_sdk._generated.common.country import Country, _deserialize_country, _serialize_country
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from portone_server_sdk._generated.payment.discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError, _deserialize_discount_amount_exceeds_total_amount_error, _serialize_discount_amount_exceeds_total_amount_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.payment.get_all_payments_by_cursor_response import GetAllPaymentsByCursorResponse, _deserialize_get_all_payments_by_cursor_response, _serialize_get_all_payments_by_cursor_response
from portone_server_sdk._generated.payment.get_payments_response import GetPaymentsResponse, _deserialize_get_payments_response, _serialize_get_payments_response
from portone_server_sdk._generated.payment.instant_payment_method_input import InstantPaymentMethodInput, _deserialize_instant_payment_method_input, _serialize_instant_payment_method_input
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.max_transaction_count_reached_error import MaxTransactionCountReachedError, _deserialize_max_transaction_count_reached_error, _serialize_max_transaction_count_reached_error
from portone_server_sdk._generated.payment.max_webhook_retry_count_reached_error import MaxWebhookRetryCountReachedError, _deserialize_max_webhook_retry_count_reached_error, _serialize_max_webhook_retry_count_reached_error
from portone_server_sdk._generated.payment.modify_escrow_logistics_response import ModifyEscrowLogisticsResponse, _deserialize_modify_escrow_logistics_response, _serialize_modify_escrow_logistics_response
from portone_server_sdk._generated.common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from portone_server_sdk._generated.payment.pay_instantly_response import PayInstantlyResponse, _deserialize_pay_instantly_response, _serialize_pay_instantly_response
from portone_server_sdk._generated.payment.pay_with_billing_key_response import PayWithBillingKeyResponse, _deserialize_pay_with_billing_key_response, _serialize_pay_with_billing_key_response
from portone_server_sdk._generated.payment.payment import Payment, _deserialize_payment, _serialize_payment
from portone_server_sdk._generated.payment.payment_already_cancelled_error import PaymentAlreadyCancelledError, _deserialize_payment_already_cancelled_error, _serialize_payment_already_cancelled_error
from portone_server_sdk._generated.common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from portone_server_sdk._generated.payment.payment_escrow_receiver_input import PaymentEscrowReceiverInput, _deserialize_payment_escrow_receiver_input, _serialize_payment_escrow_receiver_input
from portone_server_sdk._generated.payment.payment_escrow_sender_input import PaymentEscrowSenderInput, _deserialize_payment_escrow_sender_input, _serialize_payment_escrow_sender_input
from portone_server_sdk._generated.payment.payment_filter_input import PaymentFilterInput, _deserialize_payment_filter_input, _serialize_payment_filter_input
from portone_server_sdk._generated.payment.payment_logistics import PaymentLogistics, _deserialize_payment_logistics, _serialize_payment_logistics
from portone_server_sdk._generated.payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from portone_server_sdk._generated.payment.payment_not_paid_error import PaymentNotPaidError, _deserialize_payment_not_paid_error, _serialize_payment_not_paid_error
from portone_server_sdk._generated.payment.payment_not_waiting_for_deposit_error import PaymentNotWaitingForDepositError, _deserialize_payment_not_waiting_for_deposit_error, _serialize_payment_not_waiting_for_deposit_error
from portone_server_sdk._generated.common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product
from portone_server_sdk._generated.common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.payment.pre_register_payment_response import PreRegisterPaymentResponse, _deserialize_pre_register_payment_response, _serialize_pre_register_payment_response
from portone_server_sdk._generated.payment.promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError, _deserialize_promotion_pay_method_does_not_match_error, _serialize_promotion_pay_method_does_not_match_error
from portone_server_sdk._generated.payment.register_store_receipt_body_item import RegisterStoreReceiptBodyItem, _deserialize_register_store_receipt_body_item, _serialize_register_store_receipt_body_item
from portone_server_sdk._generated.payment.register_store_receipt_response import RegisterStoreReceiptResponse, _deserialize_register_store_receipt_response, _serialize_register_store_receipt_response
from portone_server_sdk._generated.payment.remained_amount_less_than_promotion_min_payment_amount_error import RemainedAmountLessThanPromotionMinPaymentAmountError, _deserialize_remained_amount_less_than_promotion_min_payment_amount_error, _serialize_remained_amount_less_than_promotion_min_payment_amount_error
from portone_server_sdk._generated.payment.resend_webhook_response import ResendWebhookResponse, _deserialize_resend_webhook_response, _serialize_resend_webhook_response
from portone_server_sdk._generated.common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input
from portone_server_sdk._generated.payment.sum_of_parts_exceeds_cancel_amount_error import SumOfPartsExceedsCancelAmountError, _deserialize_sum_of_parts_exceeds_cancel_amount_error, _serialize_sum_of_parts_exceeds_cancel_amount_error
from portone_server_sdk._generated.common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.payment.webhook_not_found_error import WebhookNotFoundError, _deserialize_webhook_not_found_error, _serialize_webhook_not_found_error
from urllib.parse import quote
from .billing_key import BillingKeyClient
from .cash_receipt import CashReceiptClient
from .payment_schedule import PaymentScheduleClient
from .promotion import PromotionClient
from portone_server_sdk._generated import errors
class PaymentClient:
    _secret: str
    _user_agent: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    billing_key: BillingKeyClient
    cash_receipt: CashReceiptClient
    payment_schedule: PaymentScheduleClient
    promotion: PromotionClient

    def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):
        self._secret = secret
        self._user_agent = user_agent
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.billing_key = BillingKeyClient(secret, user_agent, base_url, store_id)
        self.cash_receipt = CashReceiptClient(secret, user_agent, base_url, store_id)
        self.payment_schedule = PaymentScheduleClient(secret, user_agent, base_url, store_id)
        self.promotion = PromotionClient(secret, user_agent, base_url, store_id)
    def pre_register_payment(
        self,
        *,
        payment_id: str,
        total_amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        currency: Optional[Currency] = None,
    ) -> PreRegisterPaymentResponse:
        """결제 정보 사전 등록

        결제 정보를 사전 등록합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            total_amount (int, optional):
                결제 총 금액
            tax_free_amount (int, optional):
                결제 면세 금액
            currency (Currency, optional):
                통화 단위


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if total_amount is not None:
            request_body["totalAmount"] = total_amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if currency is not None:
            request_body["currency"] = _serialize_currency(currency)
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/pre-register",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pre_register_payment_response(response.json())
    async def pre_register_payment_async(
        self,
        *,
        payment_id: str,
        total_amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        currency: Optional[Currency] = None,
    ) -> PreRegisterPaymentResponse:
        """결제 정보 사전 등록

        결제 정보를 사전 등록합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            total_amount (int, optional):
                결제 총 금액
            tax_free_amount (int, optional):
                결제 면세 금액
            currency (Currency, optional):
                통화 단위


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if total_amount is not None:
            request_body["totalAmount"] = total_amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if currency is not None:
            request_body["currency"] = _serialize_currency(currency)
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/pre-register",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pre_register_payment_response(response.json())
    def get_payment(
        self,
        *,
        payment_id: str,
    ) -> Payment:
        """결제 단건 조회

        주어진 아이디에 대응되는 결제 건을 조회합니다.

        Args:
            payment_id (str):
                조회할 결제 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_payment(response.json())
    async def get_payment_async(
        self,
        *,
        payment_id: str,
    ) -> Payment:
        """결제 단건 조회

        주어진 아이디에 대응되는 결제 건을 조회합니다.

        Args:
            payment_id (str):
                조회할 결제 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_payment(response.json())
    def get_payments(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PaymentFilterInput] = None,
    ) -> GetPaymentsResponse:
        """결제 다건 조회(페이지 기반)

        주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            filter (PaymentFilterInput, optional):
                조회할 결제 건 조건 필터

                V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_payment_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payments",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_payments_response(response.json())
    async def get_payments_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PaymentFilterInput] = None,
    ) -> GetPaymentsResponse:
        """결제 다건 조회(페이지 기반)

        주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보

                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            filter (PaymentFilterInput, optional):
                조회할 결제 건 조건 필터

                V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_payment_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payments",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_payments_response(response.json())
    def get_all_payments_by_cursor(
        self,
        *,
        from_: Optional[str] = None,
        until: Optional[str] = None,
        cursor: Optional[str] = None,
        size: Optional[int] = None,
    ) -> GetAllPaymentsByCursorResponse:
        """결제 대용량 다건 조회(커서 기반)

        기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.

        Args:
            from_ (str, optional):
                결제 건 생성시점 범위 조건의 시작

                값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
            until (str, optional):
                결제 건 생성시점 범위 조건의 끝

                값을 입력하지 않으면 현재 시점으로 설정됩니다.
            cursor (str, optional):
                커서

                결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
            size (int, optional):
                페이지 크기

                미입력 시 기본값은 10 이며 최대 1000까지 허용


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if from_ is not None:
            request_body["from"] = from_
        if until is not None:
            request_body["until"] = until
        if cursor is not None:
            request_body["cursor"] = cursor
        if size is not None:
            request_body["size"] = size
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payments-by-cursor",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_all_payments_by_cursor_response(response.json())
    async def get_all_payments_by_cursor_async(
        self,
        *,
        from_: Optional[str] = None,
        until: Optional[str] = None,
        cursor: Optional[str] = None,
        size: Optional[int] = None,
    ) -> GetAllPaymentsByCursorResponse:
        """결제 대용량 다건 조회(커서 기반)

        기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.

        Args:
            from_ (str, optional):
                결제 건 생성시점 범위 조건의 시작

                값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
            until (str, optional):
                결제 건 생성시점 범위 조건의 끝

                값을 입력하지 않으면 현재 시점으로 설정됩니다.
            cursor (str, optional):
                커서

                결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
            size (int, optional):
                페이지 크기

                미입력 시 기본값은 10 이며 최대 1000까지 허용


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if from_ is not None:
            request_body["from"] = from_
        if until is not None:
            request_body["until"] = until
        if cursor is not None:
            request_body["cursor"] = cursor
        if size is not None:
            request_body["size"] = size
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payments-by-cursor",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_get_all_payments_by_cursor_response(response.json())
    def cancel_payment(
        self,
        *,
        payment_id: str,
        amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        vat_amount: Optional[int] = None,
        reason: str,
        requester: Optional[CancelRequester] = None,
        current_cancellable_amount: Optional[int] = None,
        refund_account: Optional[CancelPaymentBodyRefundAccount] = None,
    ) -> CancelPaymentResponse:
        """결제 취소

        결제 취소를 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            amount (int, optional):
                취소 총 금액

                값을 입력하지 않으면 전액 취소됩니다.
            tax_free_amount (int, optional):
                취소 금액 중 면세 금액

                값을 입력하지 않으면 전액 과세 취소됩니다.
            vat_amount (int, optional):
                취소 금액 중 부가세액

                값을 입력하지 않으면 자동 계산됩니다.
            reason (str):
                취소 사유
            requester (CancelRequester, optional):
                취소 요청자

                고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
            current_cancellable_amount (int, optional):
                결제 건의 취소 가능 잔액

                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (CancelPaymentBodyRefundAccount, optional):
                환불 계좌

                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.


        Raises:
            CancellableAmountConsistencyBrokenError: 취소 가능 잔액 검증에 실패한 경우
                취소 가능 잔액 검증에 실패한 경우
            CancelAmountExceedsCancellableAmountError: 결제 취소 금액이 취소 가능 금액을 초과한 경우
                결제 취소 금액이 취소 가능 금액을 초과한 경우
            CancelTaxAmountExceedsCancellableTaxAmountError: 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
                취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
            CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError: 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
                취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentAlreadyCancelledError: 결제가 이미 취소된 경우
                결제가 이미 취소된 경우
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            RemainedAmountLessThanPromotionMinPaymentAmountError: 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
                부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
            SumOfPartsExceedsCancelAmountError: 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if amount is not None:
            request_body["amount"] = amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if vat_amount is not None:
            request_body["vatAmount"] = vat_amount
        request_body["reason"] = reason
        if requester is not None:
            request_body["requester"] = _serialize_cancel_requester(requester)
        if current_cancellable_amount is not None:
            request_body["currentCancellableAmount"] = current_cancellable_amount
        if refund_account is not None:
            request_body["refundAccount"] = _serialize_cancel_payment_body_refund_account(refund_account)
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cancel",
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
            if error_type == "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN":
                raise errors.CancellableAmountConsistencyBrokenError(_deserialize_cancellable_amount_consistency_broken_error(error_response))
            if error_type == "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT":
                raise errors.CancelAmountExceedsCancellableAmountError(_deserialize_cancel_amount_exceeds_cancellable_amount_error(error_response))
            if error_type == "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT":
                raise errors.CancelTaxAmountExceedsCancellableTaxAmountError(_deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(error_response))
            if error_type == "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT":
                raise errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(_deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_ALREADY_CANCELLED":
                raise errors.PaymentAlreadyCancelledError(_deserialize_payment_already_cancelled_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT":
                raise errors.RemainedAmountLessThanPromotionMinPaymentAmountError(_deserialize_remained_amount_less_than_promotion_min_payment_amount_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT":
                raise errors.SumOfPartsExceedsCancelAmountError(_deserialize_sum_of_parts_exceeds_cancel_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_payment_response(response.json())
    async def cancel_payment_async(
        self,
        *,
        payment_id: str,
        amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        vat_amount: Optional[int] = None,
        reason: str,
        requester: Optional[CancelRequester] = None,
        current_cancellable_amount: Optional[int] = None,
        refund_account: Optional[CancelPaymentBodyRefundAccount] = None,
    ) -> CancelPaymentResponse:
        """결제 취소

        결제 취소를 요청합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            amount (int, optional):
                취소 총 금액

                값을 입력하지 않으면 전액 취소됩니다.
            tax_free_amount (int, optional):
                취소 금액 중 면세 금액

                값을 입력하지 않으면 전액 과세 취소됩니다.
            vat_amount (int, optional):
                취소 금액 중 부가세액

                값을 입력하지 않으면 자동 계산됩니다.
            reason (str):
                취소 사유
            requester (CancelRequester, optional):
                취소 요청자

                고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
            current_cancellable_amount (int, optional):
                결제 건의 취소 가능 잔액

                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (CancelPaymentBodyRefundAccount, optional):
                환불 계좌

                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.


        Raises:
            CancellableAmountConsistencyBrokenError: 취소 가능 잔액 검증에 실패한 경우
                취소 가능 잔액 검증에 실패한 경우
            CancelAmountExceedsCancellableAmountError: 결제 취소 금액이 취소 가능 금액을 초과한 경우
                결제 취소 금액이 취소 가능 금액을 초과한 경우
            CancelTaxAmountExceedsCancellableTaxAmountError: 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
                취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
            CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError: 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
                취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentAlreadyCancelledError: 결제가 이미 취소된 경우
                결제가 이미 취소된 경우
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            RemainedAmountLessThanPromotionMinPaymentAmountError: 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
                부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
            SumOfPartsExceedsCancelAmountError: 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if amount is not None:
            request_body["amount"] = amount
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if vat_amount is not None:
            request_body["vatAmount"] = vat_amount
        request_body["reason"] = reason
        if requester is not None:
            request_body["requester"] = _serialize_cancel_requester(requester)
        if current_cancellable_amount is not None:
            request_body["currentCancellableAmount"] = current_cancellable_amount
        if refund_account is not None:
            request_body["refundAccount"] = _serialize_cancel_payment_body_refund_account(refund_account)
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/cancel",
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
            if error_type == "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN":
                raise errors.CancellableAmountConsistencyBrokenError(_deserialize_cancellable_amount_consistency_broken_error(error_response))
            if error_type == "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT":
                raise errors.CancelAmountExceedsCancellableAmountError(_deserialize_cancel_amount_exceeds_cancellable_amount_error(error_response))
            if error_type == "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT":
                raise errors.CancelTaxAmountExceedsCancellableTaxAmountError(_deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(error_response))
            if error_type == "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT":
                raise errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(_deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_ALREADY_CANCELLED":
                raise errors.PaymentAlreadyCancelledError(_deserialize_payment_already_cancelled_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT":
                raise errors.RemainedAmountLessThanPromotionMinPaymentAmountError(_deserialize_remained_amount_less_than_promotion_min_payment_amount_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT":
                raise errors.SumOfPartsExceedsCancelAmountError(_deserialize_sum_of_parts_exceeds_cancel_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_cancel_payment_response(response.json())
    def pay_with_billing_key(
        self,
        *,
        payment_id: str,
        billing_key: str,
        channel_key: Optional[str] = None,
        order_name: str,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        installment_month: Optional[int] = None,
        use_free_interest_from_merchant: Optional[bool] = None,
        use_card_point: Optional[bool] = None,
        cash_receipt: Optional[CashReceiptInput] = None,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
        bypass: dict,
    ) -> PayWithBillingKeyResponse:
        """빌링키 결제

        빌링키로 결제를 진행합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            billing_key (str):
                빌링키 결제에 사용할 빌링키
            channel_key (str, optional):
                채널 키

                다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
            order_name (str):
                주문명
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            amount (PaymentAmountInput):
                결제 금액 세부 입력 정보
            currency (Currency):
                통화
            installment_month (int, optional):
                할부 개월 수
            use_free_interest_from_merchant (bool, optional):
                무이자 할부 이자를 고객사가 부담할지 여부
            use_card_point (bool, optional):
                카드 포인트 사용 여부
            cash_receipt (CashReceiptInput, optional):
                현금영수증 정보
            country (Country, optional):
                결제 국가
            notice_urls (list[str], optional):
                웹훅 주소

                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (list[PaymentProduct], optional):
                상품 정보

                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (int, optional):
                상품 개수
            product_type (PaymentProductType, optional):
                상품 유형
            shipping_address (SeparatedAddressInput, optional):
                배송지 주소
            promotion_id (str, optional):
                해당 결제에 적용할 프로모션 아이디
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
                프로모션 할인 금액이 결제 시도 금액 이상인 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
                결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingKey"] = billing_key
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        request_body["orderName"] = order_name
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        request_body["amount"] = _serialize_payment_amount_input(amount)
        request_body["currency"] = _serialize_currency(currency)
        if installment_month is not None:
            request_body["installmentMonth"] = installment_month
        if use_free_interest_from_merchant is not None:
            request_body["useFreeInterestFromMerchant"] = use_free_interest_from_merchant
        if use_card_point is not None:
            request_body["useCardPoint"] = use_card_point
        if cash_receipt is not None:
            request_body["cashReceipt"] = _serialize_cash_receipt_input(cash_receipt)
        if country is not None:
            request_body["country"] = _serialize_country(country)
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        if products is not None:
            request_body["products"] = products
        if product_count is not None:
            request_body["productCount"] = product_count
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        if shipping_address is not None:
            request_body["shippingAddress"] = _serialize_separated_address_input(shipping_address)
        if promotion_id is not None:
            request_body["promotionId"] = promotion_id
        if bypass is not None:
            request_body["bypass"] = bypass
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/billing-key",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
                raise errors.DiscountAmountExceedsTotalAmountError(_deserialize_discount_amount_exceeds_total_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
                raise errors.PromotionPayMethodDoesNotMatchError(_deserialize_promotion_pay_method_does_not_match_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pay_with_billing_key_response(response.json())
    async def pay_with_billing_key_async(
        self,
        *,
        payment_id: str,
        billing_key: str,
        channel_key: Optional[str] = None,
        order_name: str,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        installment_month: Optional[int] = None,
        use_free_interest_from_merchant: Optional[bool] = None,
        use_card_point: Optional[bool] = None,
        cash_receipt: Optional[CashReceiptInput] = None,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
        bypass: dict,
    ) -> PayWithBillingKeyResponse:
        """빌링키 결제

        빌링키로 결제를 진행합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            billing_key (str):
                빌링키 결제에 사용할 빌링키
            channel_key (str, optional):
                채널 키

                다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
            order_name (str):
                주문명
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            amount (PaymentAmountInput):
                결제 금액 세부 입력 정보
            currency (Currency):
                통화
            installment_month (int, optional):
                할부 개월 수
            use_free_interest_from_merchant (bool, optional):
                무이자 할부 이자를 고객사가 부담할지 여부
            use_card_point (bool, optional):
                카드 포인트 사용 여부
            cash_receipt (CashReceiptInput, optional):
                현금영수증 정보
            country (Country, optional):
                결제 국가
            notice_urls (list[str], optional):
                웹훅 주소

                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (list[PaymentProduct], optional):
                상품 정보

                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (int, optional):
                상품 개수
            product_type (PaymentProductType, optional):
                상품 유형
            shipping_address (SeparatedAddressInput, optional):
                배송지 주소
            promotion_id (str, optional):
                해당 결제에 적용할 프로모션 아이디
            bypass (dict, optional):
                PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
                빌링키가 이미 삭제된 경우
            BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
                빌링키가 존재하지 않는 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
                프로모션 할인 금액이 결제 시도 금액 이상인 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
                결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        request_body["billingKey"] = billing_key
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        request_body["orderName"] = order_name
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        request_body["amount"] = _serialize_payment_amount_input(amount)
        request_body["currency"] = _serialize_currency(currency)
        if installment_month is not None:
            request_body["installmentMonth"] = installment_month
        if use_free_interest_from_merchant is not None:
            request_body["useFreeInterestFromMerchant"] = use_free_interest_from_merchant
        if use_card_point is not None:
            request_body["useCardPoint"] = use_card_point
        if cash_receipt is not None:
            request_body["cashReceipt"] = _serialize_cash_receipt_input(cash_receipt)
        if country is not None:
            request_body["country"] = _serialize_country(country)
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        if products is not None:
            request_body["products"] = products
        if product_count is not None:
            request_body["productCount"] = product_count
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        if shipping_address is not None:
            request_body["shippingAddress"] = _serialize_separated_address_input(shipping_address)
        if promotion_id is not None:
            request_body["promotionId"] = promotion_id
        if bypass is not None:
            request_body["bypass"] = bypass
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/billing-key",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "BILLING_KEY_ALREADY_DELETED":
                raise errors.BillingKeyAlreadyDeletedError(_deserialize_billing_key_already_deleted_error(error_response))
            if error_type == "BILLING_KEY_NOT_FOUND":
                raise errors.BillingKeyNotFoundError(_deserialize_billing_key_not_found_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
                raise errors.DiscountAmountExceedsTotalAmountError(_deserialize_discount_amount_exceeds_total_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
                raise errors.PromotionPayMethodDoesNotMatchError(_deserialize_promotion_pay_method_does_not_match_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pay_with_billing_key_response(response.json())
    def pay_instantly(
        self,
        *,
        payment_id: str,
        channel_key: Optional[str] = None,
        channel_group_id: Optional[str] = None,
        method: InstantPaymentMethodInput,
        order_name: str,
        is_cultural_expense: Optional[bool] = None,
        is_escrow: Optional[bool] = None,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
    ) -> PayInstantlyResponse:
        """수기 결제

        수기 결제를 진행합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            channel_key (str, optional):
                채널 키

                채널 키 또는 채널 그룹 ID 필수
            channel_group_id (str, optional):
                채널 그룹 ID

                채널 키 또는 채널 그룹 ID 필수
            method (InstantPaymentMethodInput):
                결제수단 정보
            order_name (str):
                주문명
            is_cultural_expense (bool, optional):
                문화비 지출 여부

                기본값은 false 입니다.
            is_escrow (bool, optional):
                에스크로 결제 여부

                기본값은 false 입니다.
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            amount (PaymentAmountInput):
                결제 금액 세부 입력 정보
            currency (Currency):
                통화
            country (Country, optional):
                결제 국가
            notice_urls (list[str], optional):
                웹훅 주소

                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (list[PaymentProduct], optional):
                상품 정보

                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (int, optional):
                상품 개수
            product_type (PaymentProductType, optional):
                상품 유형
            shipping_address (SeparatedAddressInput, optional):
                배송지 주소
            promotion_id (str, optional):
                해당 결제에 적용할 프로모션 아이디


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
                프로모션 할인 금액이 결제 시도 금액 이상인 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
                결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        if channel_group_id is not None:
            request_body["channelGroupId"] = channel_group_id
        request_body["method"] = _serialize_instant_payment_method_input(method)
        request_body["orderName"] = order_name
        if is_cultural_expense is not None:
            request_body["isCulturalExpense"] = is_cultural_expense
        if is_escrow is not None:
            request_body["isEscrow"] = is_escrow
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        request_body["amount"] = _serialize_payment_amount_input(amount)
        request_body["currency"] = _serialize_currency(currency)
        if country is not None:
            request_body["country"] = _serialize_country(country)
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        if products is not None:
            request_body["products"] = products
        if product_count is not None:
            request_body["productCount"] = product_count
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        if shipping_address is not None:
            request_body["shippingAddress"] = _serialize_separated_address_input(shipping_address)
        if promotion_id is not None:
            request_body["promotionId"] = promotion_id
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/instant",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
                raise errors.DiscountAmountExceedsTotalAmountError(_deserialize_discount_amount_exceeds_total_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
                raise errors.PromotionPayMethodDoesNotMatchError(_deserialize_promotion_pay_method_does_not_match_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pay_instantly_response(response.json())
    async def pay_instantly_async(
        self,
        *,
        payment_id: str,
        channel_key: Optional[str] = None,
        channel_group_id: Optional[str] = None,
        method: InstantPaymentMethodInput,
        order_name: str,
        is_cultural_expense: Optional[bool] = None,
        is_escrow: Optional[bool] = None,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
    ) -> PayInstantlyResponse:
        """수기 결제

        수기 결제를 진행합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            channel_key (str, optional):
                채널 키

                채널 키 또는 채널 그룹 ID 필수
            channel_group_id (str, optional):
                채널 그룹 ID

                채널 키 또는 채널 그룹 ID 필수
            method (InstantPaymentMethodInput):
                결제수단 정보
            order_name (str):
                주문명
            is_cultural_expense (bool, optional):
                문화비 지출 여부

                기본값은 false 입니다.
            is_escrow (bool, optional):
                에스크로 결제 여부

                기본값은 false 입니다.
            customer (CustomerInput, optional):
                고객 정보
            custom_data (str, optional):
                사용자 지정 데이터
            amount (PaymentAmountInput):
                결제 금액 세부 입력 정보
            currency (Currency):
                통화
            country (Country, optional):
                결제 국가
            notice_urls (list[str], optional):
                웹훅 주소

                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (list[PaymentProduct], optional):
                상품 정보

                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (int, optional):
                상품 개수
            product_type (PaymentProductType, optional):
                상품 유형
            shipping_address (SeparatedAddressInput, optional):
                배송지 주소
            promotion_id (str, optional):
                해당 결제에 적용할 프로모션 아이디


        Raises:
            AlreadyPaidError: 결제가 이미 완료된 경우
                결제가 이미 완료된 경우
            ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
                요청된 채널이 존재하지 않는 경우
            DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
                프로모션 할인 금액이 결제 시도 금액 이상인 경우
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxTransactionCountReachedError: 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
                결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
            PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
                결제 예약건이 이미 존재하는 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
                결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
                면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if channel_key is not None:
            request_body["channelKey"] = channel_key
        if channel_group_id is not None:
            request_body["channelGroupId"] = channel_group_id
        request_body["method"] = _serialize_instant_payment_method_input(method)
        request_body["orderName"] = order_name
        if is_cultural_expense is not None:
            request_body["isCulturalExpense"] = is_cultural_expense
        if is_escrow is not None:
            request_body["isEscrow"] = is_escrow
        if customer is not None:
            request_body["customer"] = _serialize_customer_input(customer)
        if custom_data is not None:
            request_body["customData"] = custom_data
        request_body["amount"] = _serialize_payment_amount_input(amount)
        request_body["currency"] = _serialize_currency(currency)
        if country is not None:
            request_body["country"] = _serialize_country(country)
        if notice_urls is not None:
            request_body["noticeUrls"] = notice_urls
        if products is not None:
            request_body["products"] = products
        if product_count is not None:
            request_body["productCount"] = product_count
        if product_type is not None:
            request_body["productType"] = _serialize_payment_product_type(product_type)
        if shipping_address is not None:
            request_body["shippingAddress"] = _serialize_separated_address_input(shipping_address)
        if promotion_id is not None:
            request_body["promotionId"] = promotion_id
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/instant",
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
            if error_type == "ALREADY_PAID":
                raise errors.AlreadyPaidError(_deserialize_already_paid_error(error_response))
            if error_type == "CHANNEL_NOT_FOUND":
                raise errors.ChannelNotFoundError(_deserialize_channel_not_found_error(error_response))
            if error_type == "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
                raise errors.DiscountAmountExceedsTotalAmountError(_deserialize_discount_amount_exceeds_total_amount_error(error_response))
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_TRANSACTION_COUNT_REACHED":
                raise errors.MaxTransactionCountReachedError(_deserialize_max_transaction_count_reached_error(error_response))
            if error_type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
                raise errors.PaymentScheduleAlreadyExistsError(_deserialize_payment_schedule_already_exists_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
                raise errors.PromotionPayMethodDoesNotMatchError(_deserialize_promotion_pay_method_does_not_match_error(error_response))
            if error_type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
                raise errors.SumOfPartsExceedsTotalAmountError(_deserialize_sum_of_parts_exceeds_total_amount_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_pay_instantly_response(response.json())
    def close_virtual_account(
        self,
        *,
        payment_id: str,
    ) -> CloseVirtualAccountResponse:
        """가상계좌 말소

        발급된 가상계좌를 말소합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotWaitingForDepositError: 결제 건이 입금 대기 상태가 아닌 경우
                결제 건이 입금 대기 상태가 아닌 경우
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
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/virtual-account/close",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_WAITING_FOR_DEPOSIT":
                raise errors.PaymentNotWaitingForDepositError(_deserialize_payment_not_waiting_for_deposit_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_close_virtual_account_response(response.json())
    async def close_virtual_account_async(
        self,
        *,
        payment_id: str,
    ) -> CloseVirtualAccountResponse:
        """가상계좌 말소

        발급된 가상계좌를 말소합니다.

        Args:
            payment_id (str):
                결제 건 아이디


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotWaitingForDepositError: 결제 건이 입금 대기 상태가 아닌 경우
                결제 건이 입금 대기 상태가 아닌 경우
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
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/virtual-account/close",
            params=query,
            headers={
                "Authorization": f"PortOne {self._secret}",
                "User-Agent": self._user_agent,
            },
        )
        if response.status_code != 200:
            error_response = response.json()
            error_type = error_response["type"]
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_WAITING_FOR_DEPOSIT":
                raise errors.PaymentNotWaitingForDepositError(_deserialize_payment_not_waiting_for_deposit_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_close_virtual_account_response(response.json())
    def apply_escrow_logistics(
        self,
        *,
        payment_id: str,
        sender: Optional[PaymentEscrowSenderInput] = None,
        receiver: Optional[PaymentEscrowReceiverInput] = None,
        logistics: PaymentLogistics,
        send_email: Optional[bool] = None,
        products: Optional[list[PaymentProduct]] = None,
    ) -> ApplyEscrowLogisticsResponse:
        """에스크로 배송 정보 등록

        에스크로 배송 정보를 등록합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            sender (PaymentEscrowSenderInput, optional):
                에스크로 발송자 정보
            receiver (PaymentEscrowReceiverInput, optional):
                에스크로 수취인 정보
            logistics (PaymentLogistics):
                에스크로 물류 정보
            send_email (bool, optional):
                이메일 알림 전송 여부

                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (list[PaymentProduct], optional):
                상품 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if sender is not None:
            request_body["sender"] = _serialize_payment_escrow_sender_input(sender)
        if receiver is not None:
            request_body["receiver"] = _serialize_payment_escrow_receiver_input(receiver)
        request_body["logistics"] = _serialize_payment_logistics(logistics)
        if send_email is not None:
            request_body["sendEmail"] = send_email
        if products is not None:
            request_body["products"] = products
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/logistics",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_apply_escrow_logistics_response(response.json())
    async def apply_escrow_logistics_async(
        self,
        *,
        payment_id: str,
        sender: Optional[PaymentEscrowSenderInput] = None,
        receiver: Optional[PaymentEscrowReceiverInput] = None,
        logistics: PaymentLogistics,
        send_email: Optional[bool] = None,
        products: Optional[list[PaymentProduct]] = None,
    ) -> ApplyEscrowLogisticsResponse:
        """에스크로 배송 정보 등록

        에스크로 배송 정보를 등록합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            sender (PaymentEscrowSenderInput, optional):
                에스크로 발송자 정보
            receiver (PaymentEscrowReceiverInput, optional):
                에스크로 수취인 정보
            logistics (PaymentLogistics):
                에스크로 물류 정보
            send_email (bool, optional):
                이메일 알림 전송 여부

                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (list[PaymentProduct], optional):
                상품 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if sender is not None:
            request_body["sender"] = _serialize_payment_escrow_sender_input(sender)
        if receiver is not None:
            request_body["receiver"] = _serialize_payment_escrow_receiver_input(receiver)
        request_body["logistics"] = _serialize_payment_logistics(logistics)
        if send_email is not None:
            request_body["sendEmail"] = send_email
        if products is not None:
            request_body["products"] = products
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/logistics",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_apply_escrow_logistics_response(response.json())
    def modify_escrow_logistics(
        self,
        *,
        payment_id: str,
        sender: Optional[PaymentEscrowSenderInput] = None,
        receiver: Optional[PaymentEscrowReceiverInput] = None,
        logistics: PaymentLogistics,
        send_email: Optional[bool] = None,
        products: Optional[list[PaymentProduct]] = None,
    ) -> ModifyEscrowLogisticsResponse:
        """에스크로 배송 정보 수정

        에스크로 배송 정보를 수정합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            sender (PaymentEscrowSenderInput, optional):
                에스크로 발송자 정보
            receiver (PaymentEscrowReceiverInput, optional):
                에스크로 수취인 정보
            logistics (PaymentLogistics):
                에스크로 물류 정보
            send_email (bool, optional):
                이메일 알림 전송 여부

                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (list[PaymentProduct], optional):
                상품 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if sender is not None:
            request_body["sender"] = _serialize_payment_escrow_sender_input(sender)
        if receiver is not None:
            request_body["receiver"] = _serialize_payment_escrow_receiver_input(receiver)
        request_body["logistics"] = _serialize_payment_logistics(logistics)
        if send_email is not None:
            request_body["sendEmail"] = send_email
        if products is not None:
            request_body["products"] = products
        query = []
        response = httpx.request(
            "PATCH",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/logistics",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_modify_escrow_logistics_response(response.json())
    async def modify_escrow_logistics_async(
        self,
        *,
        payment_id: str,
        sender: Optional[PaymentEscrowSenderInput] = None,
        receiver: Optional[PaymentEscrowReceiverInput] = None,
        logistics: PaymentLogistics,
        send_email: Optional[bool] = None,
        products: Optional[list[PaymentProduct]] = None,
    ) -> ModifyEscrowLogisticsResponse:
        """에스크로 배송 정보 수정

        에스크로 배송 정보를 수정합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            sender (PaymentEscrowSenderInput, optional):
                에스크로 발송자 정보
            receiver (PaymentEscrowReceiverInput, optional):
                에스크로 수취인 정보
            logistics (PaymentLogistics):
                에스크로 물류 정보
            send_email (bool, optional):
                이메일 알림 전송 여부

                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (list[PaymentProduct], optional):
                상품 정보


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if sender is not None:
            request_body["sender"] = _serialize_payment_escrow_sender_input(sender)
        if receiver is not None:
            request_body["receiver"] = _serialize_payment_escrow_receiver_input(receiver)
        request_body["logistics"] = _serialize_payment_logistics(logistics)
        if send_email is not None:
            request_body["sendEmail"] = send_email
        if products is not None:
            request_body["products"] = products
        query = []
        response = await self._client.request(
            "PATCH",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/logistics",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_modify_escrow_logistics_response(response.json())
    def confirm_escrow(
        self,
        *,
        payment_id: str,
        from_store: Optional[bool] = None,
    ) -> ConfirmEscrowResponse:
        """에스크로 구매 확정

        에스크로 결제를 구매 확정 처리합니다

        Args:
            payment_id (str):
                결제 건 아이디
            from_store (bool, optional):
                확인 주체가 상점인지 여부

                구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
                네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if from_store is not None:
            request_body["fromStore"] = from_store
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/complete",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_confirm_escrow_response(response.json())
    async def confirm_escrow_async(
        self,
        *,
        payment_id: str,
        from_store: Optional[bool] = None,
    ) -> ConfirmEscrowResponse:
        """에스크로 구매 확정

        에스크로 결제를 구매 확정 처리합니다

        Args:
            payment_id (str):
                결제 건 아이디
            from_store (bool, optional):
                확인 주체가 상점인지 여부

                구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
                네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if from_store is not None:
            request_body["fromStore"] = from_store
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/escrow/complete",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_confirm_escrow_response(response.json())
    def resend_webhook(
        self,
        *,
        payment_id: str,
        webhook_id: Optional[str] = None,
    ) -> ResendWebhookResponse:
        """웹훅 재발송

        웹훅을 재발송합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            webhook_id (str, optional):
                웹훅 아이디

                입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxWebhookRetryCountReachedError: 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우
                동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            WebhookNotFoundError: 웹훅 내역이 존재하지 않는 경우
                웹훅 내역이 존재하지 않는 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if webhook_id is not None:
            request_body["webhookId"] = webhook_id
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/resend-webhook",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_WEBHOOK_RETRY_COUNT_REACHED":
                raise errors.MaxWebhookRetryCountReachedError(_deserialize_max_webhook_retry_count_reached_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            if error_type == "WEBHOOK_NOT_FOUND":
                raise errors.WebhookNotFoundError(_deserialize_webhook_not_found_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_resend_webhook_response(response.json())
    async def resend_webhook_async(
        self,
        *,
        payment_id: str,
        webhook_id: Optional[str] = None,
    ) -> ResendWebhookResponse:
        """웹훅 재발송

        웹훅을 재발송합니다.

        Args:
            payment_id (str):
                결제 건 아이디
            webhook_id (str, optional):
                웹훅 아이디

                입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            MaxWebhookRetryCountReachedError: 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우
                동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            WebhookNotFoundError: 웹훅 내역이 존재하지 않는 경우
                웹훅 내역이 존재하지 않는 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        if webhook_id is not None:
            request_body["webhookId"] = webhook_id
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/resend-webhook",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "MAX_WEBHOOK_RETRY_COUNT_REACHED":
                raise errors.MaxWebhookRetryCountReachedError(_deserialize_max_webhook_retry_count_reached_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            if error_type == "WEBHOOK_NOT_FOUND":
                raise errors.WebhookNotFoundError(_deserialize_webhook_not_found_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_resend_webhook_response(response.json())
    def register_store_receipt(
        self,
        *,
        payment_id: str,
        items: list[RegisterStoreReceiptBodyItem],
    ) -> RegisterStoreReceiptResponse:
        """영수증 내 하위 상점 거래 등록

        결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
        지원되는 PG사:
        KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)

        Args:
            payment_id (str):
                등록할 하위 상점 결제 건 아이디
            items (list[RegisterStoreReceiptBodyItem]):
                하위 상점 거래 목록


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["items"] = items
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/register-store-receipt",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_register_store_receipt_response(response.json())
    async def register_store_receipt_async(
        self,
        *,
        payment_id: str,
        items: list[RegisterStoreReceiptBodyItem],
    ) -> RegisterStoreReceiptResponse:
        """영수증 내 하위 상점 거래 등록

        결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
        지원되는 PG사:
        KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)

        Args:
            payment_id (str):
                등록할 하위 상점 결제 건 아이디
            items (list[RegisterStoreReceiptBodyItem]):
                하위 상점 거래 목록


        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
                요청된 입력 정보가 유효하지 않은 경우

                허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
            PaymentNotFoundError: 결제 건이 존재하지 않는 경우
                결제 건이 존재하지 않는 경우
            PaymentNotPaidError: 결제가 완료되지 않은 경우
                결제가 완료되지 않은 경우
            PgProviderError: PG사에서 오류를 전달한 경우
                PG사에서 오류를 전달한 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        request_body = {}
        request_body["items"] = items
        if self._store_id is not None:
            request_body["storeId"] = self._store_id
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/register-store-receipt",
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
            if error_type == "FORBIDDEN":
                raise errors.ForbiddenError(_deserialize_forbidden_error(error_response))
            if error_type == "INVALID_REQUEST":
                raise errors.InvalidRequestError(_deserialize_invalid_request_error(error_response))
            if error_type == "PAYMENT_NOT_FOUND":
                raise errors.PaymentNotFoundError(_deserialize_payment_not_found_error(error_response))
            if error_type == "PAYMENT_NOT_PAID":
                raise errors.PaymentNotPaidError(_deserialize_payment_not_paid_error(error_response))
            if error_type == "PG_PROVIDER":
                raise errors.PgProviderError(_deserialize_pg_provider_error(error_response))
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_register_store_receipt_response(response.json())
