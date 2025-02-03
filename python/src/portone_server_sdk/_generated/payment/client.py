from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import AlreadyPaidError, BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, CancelAmountExceedsCancellableAmountError, CancelTaxAmountExceedsCancellableTaxAmountError, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError, CancellableAmountConsistencyBrokenError, ChannelNotFoundError, DiscountAmountExceedsTotalAmountError, ForbiddenError, InvalidRequestError, MaxTransactionCountReachedError, MaxWebhookRetryCountReachedError, NegativePromotionAdjustedCancelAmountError, PaymentAlreadyCancelledError, PaymentNotFoundError, PaymentNotPaidError, PaymentNotWaitingForDepositError, PaymentScheduleAlreadyExistsError, PgProviderError, PromotionDiscountRetainOptionShouldNotBeChangedError, PromotionPayMethodDoesNotMatchError, SumOfPartsExceedsCancelAmountError, SumOfPartsExceedsTotalAmountError, UnauthorizedError, UnknownError, WebhookNotFoundError
from ..payment.already_paid_error import _deserialize_already_paid_error
from ..common.billing_key_already_deleted_error import _deserialize_billing_key_already_deleted_error
from ..common.billing_key_not_found_error import _deserialize_billing_key_not_found_error
from ..payment.cancel_amount_exceeds_cancellable_amount_error import _deserialize_cancel_amount_exceeds_cancellable_amount_error
from ..payment.cancel_tax_amount_exceeds_cancellable_tax_amount_error import _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error
from ..payment.cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error
from ..payment.cancellable_amount_consistency_broken_error import _deserialize_cancellable_amount_consistency_broken_error
from ..common.channel_not_found_error import _deserialize_channel_not_found_error
from ..payment.discount_amount_exceeds_total_amount_error import _deserialize_discount_amount_exceeds_total_amount_error
from ..common.forbidden_error import _deserialize_forbidden_error
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.max_transaction_count_reached_error import _deserialize_max_transaction_count_reached_error
from ..payment.max_webhook_retry_count_reached_error import _deserialize_max_webhook_retry_count_reached_error
from ..payment.negative_promotion_adjusted_cancel_amount_error import _deserialize_negative_promotion_adjusted_cancel_amount_error
from ..payment.payment_already_cancelled_error import _deserialize_payment_already_cancelled_error
from ..payment.payment_not_found_error import _deserialize_payment_not_found_error
from ..payment.payment_not_paid_error import _deserialize_payment_not_paid_error
from ..payment.payment_not_waiting_for_deposit_error import _deserialize_payment_not_waiting_for_deposit_error
from ..common.payment_schedule_already_exists_error import _deserialize_payment_schedule_already_exists_error
from ..common.pg_provider_error import _deserialize_pg_provider_error
from ..payment.promotion_discount_retain_option_should_not_be_changed_error import _deserialize_promotion_discount_retain_option_should_not_be_changed_error
from ..payment.promotion_pay_method_does_not_match_error import _deserialize_promotion_pay_method_does_not_match_error
from ..payment.sum_of_parts_exceeds_cancel_amount_error import _deserialize_sum_of_parts_exceeds_cancel_amount_error
from ..common.sum_of_parts_exceeds_total_amount_error import _deserialize_sum_of_parts_exceeds_total_amount_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..payment.webhook_not_found_error import _deserialize_webhook_not_found_error
from ..payment.apply_escrow_logistics_response import ApplyEscrowLogisticsResponse, _deserialize_apply_escrow_logistics_response, _serialize_apply_escrow_logistics_response
from ..payment.cancel_payment_body_refund_account import CancelPaymentBodyRefundAccount, _deserialize_cancel_payment_body_refund_account, _serialize_cancel_payment_body_refund_account
from ..payment.cancel_payment_response import CancelPaymentResponse, _deserialize_cancel_payment_response, _serialize_cancel_payment_response
from ..payment.cancel_requester import CancelRequester, _deserialize_cancel_requester, _serialize_cancel_requester
from ..common.cash_receipt_input import CashReceiptInput, _deserialize_cash_receipt_input, _serialize_cash_receipt_input
from ..payment.close_virtual_account_response import CloseVirtualAccountResponse, _deserialize_close_virtual_account_response, _serialize_close_virtual_account_response
from ..payment.confirm_escrow_response import ConfirmEscrowResponse, _deserialize_confirm_escrow_response, _serialize_confirm_escrow_response
from ..common.country import Country, _deserialize_country, _serialize_country
from ..common.currency import Currency, _deserialize_currency, _serialize_currency
from ..common.customer_input import CustomerInput, _deserialize_customer_input, _serialize_customer_input
from ..payment.get_all_payments_by_cursor_response import GetAllPaymentsByCursorResponse, _deserialize_get_all_payments_by_cursor_response, _serialize_get_all_payments_by_cursor_response
from ..payment.get_payment_transactions_response import GetPaymentTransactionsResponse, _deserialize_get_payment_transactions_response, _serialize_get_payment_transactions_response
from ..payment.get_payments_response import GetPaymentsResponse, _deserialize_get_payments_response, _serialize_get_payments_response
from ..payment.instant_payment_method_input import InstantPaymentMethodInput, _deserialize_instant_payment_method_input, _serialize_instant_payment_method_input
from ..payment.modify_escrow_logistics_response import ModifyEscrowLogisticsResponse, _deserialize_modify_escrow_logistics_response, _serialize_modify_escrow_logistics_response
from ..common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ..payment.pay_instantly_response import PayInstantlyResponse, _deserialize_pay_instantly_response, _serialize_pay_instantly_response
from ..payment.pay_with_billing_key_response import PayWithBillingKeyResponse, _deserialize_pay_with_billing_key_response, _serialize_pay_with_billing_key_response
from ..payment.payment import Payment, _deserialize_payment, _serialize_payment
from ..common.payment_amount_input import PaymentAmountInput, _deserialize_payment_amount_input, _serialize_payment_amount_input
from ..payment.payment_escrow_receiver_input import PaymentEscrowReceiverInput, _deserialize_payment_escrow_receiver_input, _serialize_payment_escrow_receiver_input
from ..payment.payment_escrow_sender_input import PaymentEscrowSenderInput, _deserialize_payment_escrow_sender_input, _serialize_payment_escrow_sender_input
from ..payment.payment_filter_input import PaymentFilterInput, _deserialize_payment_filter_input, _serialize_payment_filter_input
from ..payment.payment_logistics import PaymentLogistics, _deserialize_payment_logistics, _serialize_payment_logistics
from ..common.payment_product import PaymentProduct, _deserialize_payment_product, _serialize_payment_product
from ..common.payment_product_type import PaymentProductType, _deserialize_payment_product_type, _serialize_payment_product_type
from ..payment.pre_register_payment_response import PreRegisterPaymentResponse, _deserialize_pre_register_payment_response, _serialize_pre_register_payment_response
from ..payment.promotion_discount_retain_option import PromotionDiscountRetainOption, _deserialize_promotion_discount_retain_option, _serialize_promotion_discount_retain_option
from ..payment.register_store_receipt_body_item import RegisterStoreReceiptBodyItem, _deserialize_register_store_receipt_body_item, _serialize_register_store_receipt_body_item
from ..payment.register_store_receipt_response import RegisterStoreReceiptResponse, _deserialize_register_store_receipt_response, _serialize_register_store_receipt_response
from ..payment.resend_webhook_response import ResendWebhookResponse, _deserialize_resend_webhook_response, _serialize_resend_webhook_response
from ..common.separated_address_input import SeparatedAddressInput, _deserialize_separated_address_input, _serialize_separated_address_input
from urllib.parse import quote
from .billing_key.client import BillingKeyClient
from .cash_receipt.client import CashReceiptClient
from .payment_schedule.client import PaymentScheduleClient
from .promotion.client import PromotionClient
class PaymentClient:
    _secret: str
    _base_url: str
    _store_id: Optional[str]
    _client: AsyncClient
    billing_key: BillingKeyClient
    cash_receipt: CashReceiptClient
    payment_schedule: PaymentScheduleClient
    promotion: PromotionClient

    def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):
        """API Secret을 사용해 포트원 API 클라이언트를 생성합니다."""
        self._secret = secret
        self._base_url = base_url
        self._store_id = store_id
        self._client = AsyncClient()
        self.billing_key = BillingKeyClient(secret=secret, base_url=base_url, store_id=store_id)
        self.cash_receipt = CashReceiptClient(secret=secret, base_url=base_url, store_id=store_id)
        self.payment_schedule = PaymentScheduleClient(secret=secret, base_url=base_url, store_id=store_id)
        self.promotion = PromotionClient(secret=secret, base_url=base_url, store_id=store_id)
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
            PreRegisterPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
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
            PreRegisterPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
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
            GetPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            GetPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
        return _deserialize_payment(response.json())
    def get_payment_transactions(
        self,
        *,
        payment_id: str,
    ) -> GetPaymentTransactionsResponse:
        """결제 시도 내역 조회

        주어진 아이디에 대응되는 결제 건의 결제 시도 내역을 조회합니다.

        Args:
            payment_id (str):
                조회할 결제 아이디


        Raises:
            GetPaymentTransactionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = httpx.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/transactions",
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
        return _deserialize_get_payment_transactions_response(response.json())
    async def get_payment_transactions_async(
        self,
        *,
        payment_id: str,
    ) -> GetPaymentTransactionsResponse:
        """결제 시도 내역 조회

        주어진 아이디에 대응되는 결제 건의 결제 시도 내역을 조회합니다.

        Args:
            payment_id (str):
                조회할 결제 아이디


        Raises:
            GetPaymentTransactionsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if self._store_id is not None:
            query.append(("storeId", self._store_id))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/payments/{quote(payment_id, safe='')}/transactions",
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
        return _deserialize_get_payment_transactions_response(response.json())
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
            GetPaymentsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            GetPaymentsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            GetAllPaymentsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
            GetAllPaymentsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
        promotion_discount_retain_option: Optional[PromotionDiscountRetainOption] = None,
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
            promotion_discount_retain_option (PromotionDiscountRetainOption, optional):
                프로모션 할인율 유지 옵션

                프로모션이 적용된 결제를 부분 취소하는 경우, 최초 할인율을 유지할지 여부를 선택할 수 있습니다.
                RETAIN 으로 설정 시, 최초 할인율을 유지할 수 있도록 취소 금액이 조정됩니다.
                RELEASE 으로 설정 시, 취소 후 남은 금액이 속한 구간에 맞게 프로모션 할인이 새롭게 적용됩니다.
                값을 입력하지 않으면 RELEASE 로 취급합니다.
            current_cancellable_amount (int, optional):
                결제 건의 취소 가능 잔액

                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (CancelPaymentBodyRefundAccount, optional):
                환불 계좌

                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.


        Raises:
            CancelPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
        if promotion_discount_retain_option is not None:
            request_body["promotionDiscountRetainOption"] = _serialize_promotion_discount_retain_option(promotion_discount_retain_option)
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_cancellable_amount_consistency_broken_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancellableAmountConsistencyBrokenError(error)
            try:
                error = _deserialize_cancel_amount_exceeds_cancellable_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelAmountExceedsCancellableAmountError(error)
            try:
                error = _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelTaxAmountExceedsCancellableTaxAmountError(error)
            try:
                error = _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(error)
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
                error = _deserialize_negative_promotion_adjusted_cancel_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise NegativePromotionAdjustedCancelAmountError(error)
            try:
                error = _deserialize_payment_already_cancelled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentAlreadyCancelledError(error)
            try:
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_discount_retain_option_should_not_be_changed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionDiscountRetainOptionShouldNotBeChangedError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_cancel_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsCancelAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
        promotion_discount_retain_option: Optional[PromotionDiscountRetainOption] = None,
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
            promotion_discount_retain_option (PromotionDiscountRetainOption, optional):
                프로모션 할인율 유지 옵션

                프로모션이 적용된 결제를 부분 취소하는 경우, 최초 할인율을 유지할지 여부를 선택할 수 있습니다.
                RETAIN 으로 설정 시, 최초 할인율을 유지할 수 있도록 취소 금액이 조정됩니다.
                RELEASE 으로 설정 시, 취소 후 남은 금액이 속한 구간에 맞게 프로모션 할인이 새롭게 적용됩니다.
                값을 입력하지 않으면 RELEASE 로 취급합니다.
            current_cancellable_amount (int, optional):
                결제 건의 취소 가능 잔액

                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (CancelPaymentBodyRefundAccount, optional):
                환불 계좌

                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.


        Raises:
            CancelPaymentError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
        if promotion_discount_retain_option is not None:
            request_body["promotionDiscountRetainOption"] = _serialize_promotion_discount_retain_option(promotion_discount_retain_option)
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_cancellable_amount_consistency_broken_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancellableAmountConsistencyBrokenError(error)
            try:
                error = _deserialize_cancel_amount_exceeds_cancellable_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelAmountExceedsCancellableAmountError(error)
            try:
                error = _deserialize_cancel_tax_amount_exceeds_cancellable_tax_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelTaxAmountExceedsCancellableTaxAmountError(error)
            try:
                error = _deserialize_cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(error)
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
                error = _deserialize_negative_promotion_adjusted_cancel_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise NegativePromotionAdjustedCancelAmountError(error)
            try:
                error = _deserialize_payment_already_cancelled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentAlreadyCancelledError(error)
            try:
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_discount_retain_option_should_not_be_changed_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionDiscountRetainOptionShouldNotBeChangedError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_cancel_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsCancelAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            PayWithBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
            try:
                error = _deserialize_billing_key_already_deleted_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyDeletedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_discount_amount_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise DiscountAmountExceedsTotalAmountError(error)
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
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
            try:
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_pay_method_does_not_match_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionPayMethodDoesNotMatchError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            PayWithBillingKeyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
            try:
                error = _deserialize_billing_key_already_deleted_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyAlreadyDeletedError(error)
            try:
                error = _deserialize_billing_key_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise BillingKeyNotFoundError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_discount_amount_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise DiscountAmountExceedsTotalAmountError(error)
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
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
            try:
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_pay_method_does_not_match_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionPayMethodDoesNotMatchError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            PayInstantlyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_discount_amount_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise DiscountAmountExceedsTotalAmountError(error)
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
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
            try:
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_pay_method_does_not_match_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionPayMethodDoesNotMatchError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            PayInstantlyError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                "User-Agent": USER_AGENT,
            },
            json=request_body,
        )
        if response.status_code != 200:
            error_response = response.json()
            error = None
            try:
                error = _deserialize_already_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise AlreadyPaidError(error)
            try:
                error = _deserialize_channel_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise ChannelNotFoundError(error)
            try:
                error = _deserialize_discount_amount_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise DiscountAmountExceedsTotalAmountError(error)
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
                error = _deserialize_max_transaction_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxTransactionCountReachedError(error)
            try:
                error = _deserialize_payment_schedule_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentScheduleAlreadyExistsError(error)
            try:
                error = _deserialize_pg_provider_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PgProviderError(error)
            try:
                error = _deserialize_promotion_pay_method_does_not_match_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PromotionPayMethodDoesNotMatchError(error)
            try:
                error = _deserialize_sum_of_parts_exceeds_total_amount_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise SumOfPartsExceedsTotalAmountError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
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
            CloseVirtualAccountError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_waiting_for_deposit_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotWaitingForDepositError(error)
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
            CloseVirtualAccountError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_waiting_for_deposit_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotWaitingForDepositError(error)
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
            ApplyEscrowLogisticsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ApplyEscrowLogisticsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ModifyEscrowLogisticsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ModifyEscrowLogisticsError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ConfirmEscrowError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ConfirmEscrowError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            ResendWebhookError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_max_webhook_retry_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxWebhookRetryCountReachedError(error)
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
            try:
                error = _deserialize_webhook_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise WebhookNotFoundError(error)
            raise UnknownError(error_response)
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
            ResendWebhookError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_max_webhook_retry_count_reached_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise MaxWebhookRetryCountReachedError(error)
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
            try:
                error = _deserialize_webhook_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise WebhookNotFoundError(error)
            raise UnknownError(error_response)
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
            RegisterStoreReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
            RegisterStoreReceiptError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
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
                error = _deserialize_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotFoundError(error)
            try:
                error = _deserialize_payment_not_paid_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PaymentNotPaidError(error)
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
        return _deserialize_register_store_receipt_response(response.json())
