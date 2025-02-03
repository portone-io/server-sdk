from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformAdditionalFeePoliciesNotFoundError, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCancelOrderTransfersExistsError, PlatformCancellableAmountExceededError, PlatformCancellableDiscountAmountExceededError, PlatformCancellableDiscountTaxFreeAmountExceededError, PlatformCancellableProductQuantityExceededError, PlatformCancellationAndPaymentTypeMismatchedError, PlatformCancellationNotFoundError, PlatformCannotSpecifyTransferError, PlatformContractNotFoundError, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCurrencyNotSupportedError, PlatformDiscountSharePoliciesNotFoundError, PlatformDiscountSharePolicyIdDuplicatedError, PlatformNotEnabledError, PlatformOrderDetailMismatchedError, PlatformOrderTransferAlreadyCancelledError, PlatformPartnerNotFoundError, PlatformPaymentNotFoundError, PlatformProductIdDuplicatedError, PlatformProductIdNotFoundError, PlatformSettlementAmountExceededError, PlatformSettlementCancelAmountExceededPortOneCancelError, PlatformSettlementParameterNotFoundError, PlatformSettlementPaymentAmountExceededPortOnePaymentError, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, PlatformTransferAlreadyExistsError, PlatformTransferDiscountSharePolicyNotFoundError, PlatformTransferNonDeletableStatusError, PlatformTransferNotFoundError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, UnknownError
from ...common.forbidden_error import _deserialize_forbidden_error
from ...common.invalid_request_error import _deserialize_invalid_request_error
from ...platform.transfer.platform_additional_fee_policies_not_found_error import _deserialize_platform_additional_fee_policies_not_found_error
from ...platform.transfer.platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from ...platform.transfer.platform_cancel_order_transfers_exists_error import _deserialize_platform_cancel_order_transfers_exists_error
from ...platform.transfer.platform_cancellable_amount_exceeded_error import _deserialize_platform_cancellable_amount_exceeded_error
from ...platform.transfer.platform_cancellable_discount_amount_exceeded_error import _deserialize_platform_cancellable_discount_amount_exceeded_error
from ...platform.transfer.platform_cancellable_discount_tax_free_amount_exceeded_error import _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error
from ...platform.transfer.platform_cancellable_product_quantity_exceeded_error import _deserialize_platform_cancellable_product_quantity_exceeded_error
from ...platform.transfer.platform_cancellation_and_payment_type_mismatched_error import _deserialize_platform_cancellation_and_payment_type_mismatched_error
from ...platform.transfer.platform_cancellation_not_found_error import _deserialize_platform_cancellation_not_found_error
from ...platform.transfer.platform_cannot_specify_transfer_error import _deserialize_platform_cannot_specify_transfer_error
from ...platform.platform_contract_not_found_error import _deserialize_platform_contract_not_found_error
from ...platform.transfer.platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from ...platform.platform_currency_not_supported_error import _deserialize_platform_currency_not_supported_error
from ...platform.transfer.platform_discount_share_policies_not_found_error import _deserialize_platform_discount_share_policies_not_found_error
from ...platform.transfer.platform_discount_share_policy_id_duplicated_error import _deserialize_platform_discount_share_policy_id_duplicated_error
from ...platform.platform_not_enabled_error import _deserialize_platform_not_enabled_error
from ...platform.transfer.platform_order_detail_mismatched_error import _deserialize_platform_order_detail_mismatched_error
from ...platform.transfer.platform_order_transfer_already_cancelled_error import _deserialize_platform_order_transfer_already_cancelled_error
from ...platform.platform_partner_not_found_error import _deserialize_platform_partner_not_found_error
from ...platform.transfer.platform_payment_not_found_error import _deserialize_platform_payment_not_found_error
from ...platform.transfer.platform_product_id_duplicated_error import _deserialize_platform_product_id_duplicated_error
from ...platform.transfer.platform_product_id_not_found_error import _deserialize_platform_product_id_not_found_error
from ...platform.transfer.platform_settlement_amount_exceeded_error import _deserialize_platform_settlement_amount_exceeded_error
from ...platform.transfer.platform_settlement_cancel_amount_exceeded_port_one_cancel_error import _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error
from ...platform.transfer.platform_settlement_parameter_not_found_error import _deserialize_platform_settlement_parameter_not_found_error
from ...platform.transfer.platform_settlement_payment_amount_exceeded_port_one_payment_error import _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error import _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_settlement_tax_free_amount_exceeded_port_one_payment_error import _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_transfer_already_exists_error import _deserialize_platform_transfer_already_exists_error
from ...platform.transfer.platform_transfer_discount_share_policy_not_found_error import _deserialize_platform_transfer_discount_share_policy_not_found_error
from ...platform.transfer.platform_transfer_non_deletable_status_error import _deserialize_platform_transfer_non_deletable_status_error
from ...platform.transfer.platform_transfer_not_found_error import _deserialize_platform_transfer_not_found_error
from ...platform.platform_user_defined_property_not_found_error import _deserialize_platform_user_defined_property_not_found_error
from ...common.unauthorized_error import _deserialize_unauthorized_error
from ...platform.transfer.create_manual_transfer_response import CreateManualTransferResponse, _deserialize_create_manual_transfer_response, _serialize_create_manual_transfer_response
from ...platform.transfer.create_order_cancel_transfer_response import CreateOrderCancelTransferResponse, _deserialize_create_order_cancel_transfer_response, _serialize_create_order_cancel_transfer_response
from ...platform.transfer.create_order_transfer_response import CreateOrderTransferResponse, _deserialize_create_order_transfer_response, _serialize_create_order_transfer_response
from ...platform.transfer.create_platform_order_cancel_transfer_body_discount import CreatePlatformOrderCancelTransferBodyDiscount, _deserialize_create_platform_order_cancel_transfer_body_discount, _serialize_create_platform_order_cancel_transfer_body_discount
from ...platform.transfer.create_platform_order_cancel_transfer_body_external_cancellation_detail import CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, _deserialize_create_platform_order_cancel_transfer_body_external_cancellation_detail, _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail
from ...platform.transfer.create_platform_order_cancel_transfer_body_order_detail import CreatePlatformOrderCancelTransferBodyOrderDetail, _deserialize_create_platform_order_cancel_transfer_body_order_detail, _serialize_create_platform_order_cancel_transfer_body_order_detail
from ...platform.transfer.create_platform_order_transfer_body_additional_fee import CreatePlatformOrderTransferBodyAdditionalFee, _deserialize_create_platform_order_transfer_body_additional_fee, _serialize_create_platform_order_transfer_body_additional_fee
from ...platform.transfer.create_platform_order_transfer_body_discount import CreatePlatformOrderTransferBodyDiscount, _deserialize_create_platform_order_transfer_body_discount, _serialize_create_platform_order_transfer_body_discount
from ...platform.transfer.create_platform_order_transfer_body_external_payment_detail import CreatePlatformOrderTransferBodyExternalPaymentDetail, _deserialize_create_platform_order_transfer_body_external_payment_detail, _serialize_create_platform_order_transfer_body_external_payment_detail
from ...platform.transfer.create_platform_order_transfer_body_order_detail import CreatePlatformOrderTransferBodyOrderDetail, _deserialize_create_platform_order_transfer_body_order_detail, _serialize_create_platform_order_transfer_body_order_detail
from ...platform.transfer.delete_platform_transfer_response import DeletePlatformTransferResponse, _deserialize_delete_platform_transfer_response, _serialize_delete_platform_transfer_response
from ...platform.transfer.get_platform_transfer_summaries_response import GetPlatformTransferSummariesResponse, _deserialize_get_platform_transfer_summaries_response, _serialize_get_platform_transfer_summaries_response
from ...common.page_input import PageInput, _deserialize_page_input, _serialize_page_input
from ...platform.transfer.platform_transfer import PlatformTransfer, _deserialize_platform_transfer, _serialize_platform_transfer
from ...platform.transfer.platform_transfer_filter_input import PlatformTransferFilterInput, _deserialize_platform_transfer_filter_input, _serialize_platform_transfer_filter_input
from ...platform.transfer.platform_transfer_sheet_field import PlatformTransferSheetField, _deserialize_platform_transfer_sheet_field, _serialize_platform_transfer_sheet_field
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value
from ...platform.transfer.transfer_parameters import TransferParameters, _deserialize_transfer_parameters, _serialize_transfer_parameters
from urllib.parse import quote
class TransferClient:
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
    def get_platform_transfer(
        self,
        *,
        id: str,
    ) -> PlatformTransfer:
        """정산건 조회

        정산건을 조회합니다.

        Args:
            id (str):
                조회하고 싶은 정산건 아이디


        Raises:
            GetPlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/transfers/{quote(id, safe='')}",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_transfer(response.json())
    async def get_platform_transfer_async(
        self,
        *,
        id: str,
    ) -> PlatformTransfer:
        """정산건 조회

        정산건을 조회합니다.

        Args:
            id (str):
                조회하고 싶은 정산건 아이디


        Raises:
            GetPlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/transfers/{quote(id, safe='')}",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_platform_transfer(response.json())
    def delete_platform_transfer(
        self,
        *,
        id: str,
    ) -> DeletePlatformTransferResponse:
        """정산건 삭제

        scheduled, in_process 상태의 정산건만 삭제가능합니다.

        Args:
            id (str):
                정산건 아이디


        Raises:
            DeletePlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = httpx.request(
            "DELETE",
            f"{self._base_url}/platform/transfers/{quote(id, safe='')}",
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
                error = _deserialize_platform_cancel_order_transfers_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancelOrderTransfersExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_transfer_non_deletable_status_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNonDeletableStatusError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_delete_platform_transfer_response(response.json())
    async def delete_platform_transfer_async(
        self,
        *,
        id: str,
    ) -> DeletePlatformTransferResponse:
        """정산건 삭제

        scheduled, in_process 상태의 정산건만 삭제가능합니다.

        Args:
            id (str):
                정산건 아이디


        Raises:
            DeletePlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        response = await self._client.request(
            "DELETE",
            f"{self._base_url}/platform/transfers/{quote(id, safe='')}",
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
                error = _deserialize_platform_cancel_order_transfers_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancelOrderTransfersExistsError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_transfer_non_deletable_status_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNonDeletableStatusError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_delete_platform_transfer_response(response.json())
    def get_platform_transfer_summaries(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
    ) -> GetPlatformTransferSummariesResponse:
        """정산건 다건 조회

        성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformTransferFilterInput, optional):
                조회할 정산건 조건 필터


        Raises:
            GetPlatformTransferSummariesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/transfer-summaries",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_platform_transfer_summaries_response(response.json())
    async def get_platform_transfer_summaries_async(
        self,
        *,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
    ) -> GetPlatformTransferSummariesResponse:
        """정산건 다건 조회

        성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.

        Args:
            page (PageInput, optional):
                요청할 페이지 정보
            filter (PlatformTransferFilterInput, optional):
                조회할 정산건 조건 필터


        Raises:
            GetPlatformTransferSummariesError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if page is not None:
            request_body["page"] = _serialize_page_input(page)
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/transfer-summaries",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_get_platform_transfer_summaries_response(response.json())
    def create_platform_order_transfer(
        self,
        *,
        partner_id: str,
        contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        payment_id: str,
        order_detail: CreatePlatformOrderTransferBodyOrderDetail,
        tax_free_amount: Optional[int] = None,
        settlement_start_date: Optional[str] = None,
        discounts: list[CreatePlatformOrderTransferBodyDiscount],
        additional_fees: list[CreatePlatformOrderTransferBodyAdditionalFee],
        external_payment_detail: Optional[CreatePlatformOrderTransferBodyExternalPaymentDetail] = None,
        is_for_test: Optional[bool] = None,
        parameters: Optional[TransferParameters] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderTransferResponse:
        """주문 정산건 생성

        성공 응답으로 생성된 주문 정산건 객체가 반환됩니다.

        Args:
            partner_id (str):
                파트너 아이디
            contract_id (str, optional):
                계약 아이디

                기본값은 파트너의 기본 계약 아이디 입니다.
            memo (str, optional):
                메모
            payment_id (str):
                결제 아이디
            order_detail (CreatePlatformOrderTransferBodyOrderDetail):
                주문 정보
            tax_free_amount (int, optional):
                주문 면세 금액

                주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
            settlement_start_date (str, optional):
                정산 시작일

                기본값은 결제 일시 입니다.
            discounts (list[CreatePlatformOrderTransferBodyDiscount]):
                할인 정보
            additional_fees (list[CreatePlatformOrderTransferBodyAdditionalFee]):
                추가 수수료 정보
            external_payment_detail (CreatePlatformOrderTransferBodyExternalPaymentDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            parameters (TransferParameters, optional):
                정산 파라미터 (실험기능)
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformOrderTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["partnerId"] = partner_id
        if contract_id is not None:
            request_body["contractId"] = contract_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["paymentId"] = payment_id
        request_body["orderDetail"] = _serialize_create_platform_order_transfer_body_order_detail(order_detail)
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        request_body["discounts"] = discounts
        request_body["additionalFees"] = additional_fees
        if external_payment_detail is not None:
            request_body["externalPaymentDetail"] = _serialize_create_platform_order_transfer_body_external_payment_detail(external_payment_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if parameters is not None:
            request_body["parameters"] = _serialize_transfer_parameters(parameters)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/transfers/order",
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
                error = _deserialize_platform_additional_fee_policies_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePoliciesNotFoundError(error)
            try:
                error = _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_discount_share_policies_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePoliciesNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPaymentNotFoundError(error)
            try:
                error = _deserialize_platform_product_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdDuplicatedError(error)
            try:
                error = _deserialize_platform_settlement_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementAmountExceededError(error)
            try:
                error = _deserialize_platform_settlement_parameter_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementParameterNotFoundError(error)
            try:
                error = _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementPaymentAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementTaxFreeAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_transfer_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_order_transfer_response(response.json())
    async def create_platform_order_transfer_async(
        self,
        *,
        partner_id: str,
        contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        payment_id: str,
        order_detail: CreatePlatformOrderTransferBodyOrderDetail,
        tax_free_amount: Optional[int] = None,
        settlement_start_date: Optional[str] = None,
        discounts: list[CreatePlatformOrderTransferBodyDiscount],
        additional_fees: list[CreatePlatformOrderTransferBodyAdditionalFee],
        external_payment_detail: Optional[CreatePlatformOrderTransferBodyExternalPaymentDetail] = None,
        is_for_test: Optional[bool] = None,
        parameters: Optional[TransferParameters] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderTransferResponse:
        """주문 정산건 생성

        성공 응답으로 생성된 주문 정산건 객체가 반환됩니다.

        Args:
            partner_id (str):
                파트너 아이디
            contract_id (str, optional):
                계약 아이디

                기본값은 파트너의 기본 계약 아이디 입니다.
            memo (str, optional):
                메모
            payment_id (str):
                결제 아이디
            order_detail (CreatePlatformOrderTransferBodyOrderDetail):
                주문 정보
            tax_free_amount (int, optional):
                주문 면세 금액

                주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
            settlement_start_date (str, optional):
                정산 시작일

                기본값은 결제 일시 입니다.
            discounts (list[CreatePlatformOrderTransferBodyDiscount]):
                할인 정보
            additional_fees (list[CreatePlatformOrderTransferBodyAdditionalFee]):
                추가 수수료 정보
            external_payment_detail (CreatePlatformOrderTransferBodyExternalPaymentDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            parameters (TransferParameters, optional):
                정산 파라미터 (실험기능)
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformOrderTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["partnerId"] = partner_id
        if contract_id is not None:
            request_body["contractId"] = contract_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["paymentId"] = payment_id
        request_body["orderDetail"] = _serialize_create_platform_order_transfer_body_order_detail(order_detail)
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        request_body["discounts"] = discounts
        request_body["additionalFees"] = additional_fees
        if external_payment_detail is not None:
            request_body["externalPaymentDetail"] = _serialize_create_platform_order_transfer_body_external_payment_detail(external_payment_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if parameters is not None:
            request_body["parameters"] = _serialize_transfer_parameters(parameters)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/transfers/order",
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
                error = _deserialize_platform_additional_fee_policies_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFeePoliciesNotFoundError(error)
            try:
                error = _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(error)
            try:
                error = _deserialize_platform_contract_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractNotFoundError(error)
            try:
                error = _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(error)
            try:
                error = _deserialize_platform_currency_not_supported_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCurrencyNotSupportedError(error)
            try:
                error = _deserialize_platform_discount_share_policies_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePoliciesNotFoundError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPaymentNotFoundError(error)
            try:
                error = _deserialize_platform_product_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdDuplicatedError(error)
            try:
                error = _deserialize_platform_settlement_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementAmountExceededError(error)
            try:
                error = _deserialize_platform_settlement_parameter_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementParameterNotFoundError(error)
            try:
                error = _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementPaymentAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementTaxFreeAmountExceededPortOnePaymentError(error)
            try:
                error = _deserialize_platform_transfer_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferAlreadyExistsError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_order_transfer_response(response.json())
    def create_platform_order_cancel_transfer(
        self,
        *,
        partner_id: Optional[str] = None,
        payment_id: Optional[str] = None,
        transfer_id: Optional[str] = None,
        cancellation_id: str,
        memo: Optional[str] = None,
        order_detail: Optional[CreatePlatformOrderCancelTransferBodyOrderDetail] = None,
        tax_free_amount: Optional[int] = None,
        discounts: list[CreatePlatformOrderCancelTransferBodyDiscount],
        settlement_start_date: Optional[str] = None,
        external_cancellation_detail: Optional[CreatePlatformOrderCancelTransferBodyExternalCancellationDetail] = None,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderCancelTransferResponse:
        """주문 취소 정산건 생성

        성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.

        Args:
            partner_id (str, optional):
                파트너 아이디
            payment_id (str, optional):
                결제 아이디
            transfer_id (str, optional):
                정산건 아이디
            cancellation_id (str):
                취소 내역 아이디
            memo (str, optional):
                메모
            order_detail (CreatePlatformOrderCancelTransferBodyOrderDetail, optional):
                주문 취소 정보
            tax_free_amount (int, optional):
                주문 취소 면세 금액

                주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
            discounts (list[CreatePlatformOrderCancelTransferBodyDiscount]):
                할인 정보
            settlement_start_date (str, optional):
                정산 시작일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
            external_cancellation_detail (CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformOrderCancelTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if partner_id is not None:
            request_body["partnerId"] = partner_id
        if payment_id is not None:
            request_body["paymentId"] = payment_id
        if transfer_id is not None:
            request_body["transferId"] = transfer_id
        request_body["cancellationId"] = cancellation_id
        if memo is not None:
            request_body["memo"] = memo
        if order_detail is not None:
            request_body["orderDetail"] = _serialize_create_platform_order_cancel_transfer_body_order_detail(order_detail)
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        request_body["discounts"] = discounts
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        if external_cancellation_detail is not None:
            request_body["externalCancellationDetail"] = _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(external_cancellation_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/transfers/order-cancel",
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
                error = _deserialize_platform_cancellable_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_discount_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableDiscountAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableDiscountTaxFreeAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_product_quantity_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableProductQuantityExceededError(error)
            try:
                error = _deserialize_platform_cancellation_and_payment_type_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellationAndPaymentTypeMismatchedError(error)
            try:
                error = _deserialize_platform_cancellation_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellationNotFoundError(error)
            try:
                error = _deserialize_platform_cannot_specify_transfer_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotSpecifyTransferError(error)
            try:
                error = _deserialize_platform_discount_share_policy_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyIdDuplicatedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_order_detail_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformOrderDetailMismatchedError(error)
            try:
                error = _deserialize_platform_order_transfer_already_cancelled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformOrderTransferAlreadyCancelledError(error)
            try:
                error = _deserialize_platform_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPaymentNotFoundError(error)
            try:
                error = _deserialize_platform_product_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdDuplicatedError(error)
            try:
                error = _deserialize_platform_product_id_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdNotFoundError(error)
            try:
                error = _deserialize_platform_settlement_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementAmountExceededError(error)
            try:
                error = _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementCancelAmountExceededPortOneCancelError(error)
            try:
                error = _deserialize_platform_transfer_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferAlreadyExistsError(error)
            try:
                error = _deserialize_platform_transfer_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_order_cancel_transfer_response(response.json())
    async def create_platform_order_cancel_transfer_async(
        self,
        *,
        partner_id: Optional[str] = None,
        payment_id: Optional[str] = None,
        transfer_id: Optional[str] = None,
        cancellation_id: str,
        memo: Optional[str] = None,
        order_detail: Optional[CreatePlatformOrderCancelTransferBodyOrderDetail] = None,
        tax_free_amount: Optional[int] = None,
        discounts: list[CreatePlatformOrderCancelTransferBodyDiscount],
        settlement_start_date: Optional[str] = None,
        external_cancellation_detail: Optional[CreatePlatformOrderCancelTransferBodyExternalCancellationDetail] = None,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderCancelTransferResponse:
        """주문 취소 정산건 생성

        성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.

        Args:
            partner_id (str, optional):
                파트너 아이디
            payment_id (str, optional):
                결제 아이디
            transfer_id (str, optional):
                정산건 아이디
            cancellation_id (str):
                취소 내역 아이디
            memo (str, optional):
                메모
            order_detail (CreatePlatformOrderCancelTransferBodyOrderDetail, optional):
                주문 취소 정보
            tax_free_amount (int, optional):
                주문 취소 면세 금액

                주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
            discounts (list[CreatePlatformOrderCancelTransferBodyDiscount]):
                할인 정보
            settlement_start_date (str, optional):
                정산 시작일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
            external_cancellation_detail (CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformOrderCancelTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if partner_id is not None:
            request_body["partnerId"] = partner_id
        if payment_id is not None:
            request_body["paymentId"] = payment_id
        if transfer_id is not None:
            request_body["transferId"] = transfer_id
        request_body["cancellationId"] = cancellation_id
        if memo is not None:
            request_body["memo"] = memo
        if order_detail is not None:
            request_body["orderDetail"] = _serialize_create_platform_order_cancel_transfer_body_order_detail(order_detail)
        if tax_free_amount is not None:
            request_body["taxFreeAmount"] = tax_free_amount
        request_body["discounts"] = discounts
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        if external_cancellation_detail is not None:
            request_body["externalCancellationDetail"] = _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(external_cancellation_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/transfers/order-cancel",
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
                error = _deserialize_platform_cancellable_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_discount_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableDiscountAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_discount_tax_free_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableDiscountTaxFreeAmountExceededError(error)
            try:
                error = _deserialize_platform_cancellable_product_quantity_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellableProductQuantityExceededError(error)
            try:
                error = _deserialize_platform_cancellation_and_payment_type_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellationAndPaymentTypeMismatchedError(error)
            try:
                error = _deserialize_platform_cancellation_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCancellationNotFoundError(error)
            try:
                error = _deserialize_platform_cannot_specify_transfer_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformCannotSpecifyTransferError(error)
            try:
                error = _deserialize_platform_discount_share_policy_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformDiscountSharePolicyIdDuplicatedError(error)
            try:
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_order_detail_mismatched_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformOrderDetailMismatchedError(error)
            try:
                error = _deserialize_platform_order_transfer_already_cancelled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformOrderTransferAlreadyCancelledError(error)
            try:
                error = _deserialize_platform_payment_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPaymentNotFoundError(error)
            try:
                error = _deserialize_platform_product_id_duplicated_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdDuplicatedError(error)
            try:
                error = _deserialize_platform_product_id_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformProductIdNotFoundError(error)
            try:
                error = _deserialize_platform_settlement_amount_exceeded_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementAmountExceededError(error)
            try:
                error = _deserialize_platform_settlement_cancel_amount_exceeded_port_one_cancel_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementCancelAmountExceededPortOneCancelError(error)
            try:
                error = _deserialize_platform_transfer_already_exists_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferAlreadyExistsError(error)
            try:
                error = _deserialize_platform_transfer_discount_share_policy_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferDiscountSharePolicyNotFoundError(error)
            try:
                error = _deserialize_platform_transfer_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformTransferNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_order_cancel_transfer_response(response.json())
    def create_platform_manual_transfer(
        self,
        *,
        partner_id: str,
        memo: Optional[str] = None,
        settlement_amount: int,
        settlement_date: str,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateManualTransferResponse:
        """수기 정산건 생성

        성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.

        Args:
            partner_id (str):
                파트너 아이디
            memo (str, optional):
                메모
            settlement_amount (int):
                정산 금액
            settlement_date (str):
                정산 일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformManualTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["partnerId"] = partner_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["settlementAmount"] = settlement_amount
        request_body["settlementDate"] = settlement_date
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = httpx.request(
            "POST",
            f"{self._base_url}/platform/transfers/manual",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_manual_transfer_response(response.json())
    async def create_platform_manual_transfer_async(
        self,
        *,
        partner_id: str,
        memo: Optional[str] = None,
        settlement_amount: int,
        settlement_date: str,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateManualTransferResponse:
        """수기 정산건 생성

        성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.

        Args:
            partner_id (str):
                파트너 아이디
            memo (str, optional):
                메모
            settlement_amount (int):
                정산 금액
            settlement_date (str):
                정산 일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                기본값은 false 입니다.
            user_defined_properties (list[PlatformUserDefinedPropertyKeyValue], optional):
                사용자 정의 속성


        Raises:
            CreatePlatformManualTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["partnerId"] = partner_id
        if memo is not None:
            request_body["memo"] = memo
        request_body["settlementAmount"] = settlement_amount
        request_body["settlementDate"] = settlement_date
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = user_defined_properties
        query = []
        response = await self._client.request(
            "POST",
            f"{self._base_url}/platform/transfers/manual",
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
                error = _deserialize_platform_not_enabled_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformNotEnabledError(error)
            try:
                error = _deserialize_platform_partner_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformPartnerNotFoundError(error)
            try:
                error = _deserialize_platform_user_defined_property_not_found_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformUserDefinedPropertyNotFoundError(error)
            try:
                error = _deserialize_unauthorized_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise UnauthorizedError(error)
            raise UnknownError(error_response)
        return _deserialize_create_manual_transfer_response(response.json())
    def download_platform_transfer_sheet(
        self,
        *,
        filter: Optional[PlatformTransferFilterInput] = None,
        fields: Optional[list[PlatformTransferSheetField]] = None,
        transfer_user_defined_property_keys: Optional[list[str]] = None,
        partner_user_defined_property_keys: Optional[list[str]] = None,
    ) -> str:
        """정산 상세 내역 다운로드

        정산 상세 내역을 csv 파일로 다운로드 합니다.

        Args:
            filter (PlatformTransferFilterInput, optional):

            fields (list[PlatformTransferSheetField], optional):
                다운로드 할 시트 컬럼
            transfer_user_defined_property_keys (list[str], optional):

            partner_user_defined_property_keys (list[str], optional):



        Raises:
            DownloadPlatformTransferSheetError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        if fields is not None:
            request_body["fields"] = fields
        if transfer_user_defined_property_keys is not None:
            request_body["transferUserDefinedPropertyKeys"] = transfer_user_defined_property_keys
        if partner_user_defined_property_keys is not None:
            request_body["partnerUserDefinedPropertyKeys"] = partner_user_defined_property_keys
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/platform/transfer-summaries/sheet-file",
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
        return response.text
    async def download_platform_transfer_sheet_async(
        self,
        *,
        filter: Optional[PlatformTransferFilterInput] = None,
        fields: Optional[list[PlatformTransferSheetField]] = None,
        transfer_user_defined_property_keys: Optional[list[str]] = None,
        partner_user_defined_property_keys: Optional[list[str]] = None,
    ) -> str:
        """정산 상세 내역 다운로드

        정산 상세 내역을 csv 파일로 다운로드 합니다.

        Args:
            filter (PlatformTransferFilterInput, optional):

            fields (list[PlatformTransferSheetField], optional):
                다운로드 할 시트 컬럼
            transfer_user_defined_property_keys (list[str], optional):

            partner_user_defined_property_keys (list[str], optional):



        Raises:
            DownloadPlatformTransferSheetError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        if fields is not None:
            request_body["fields"] = fields
        if transfer_user_defined_property_keys is not None:
            request_body["transferUserDefinedPropertyKeys"] = transfer_user_defined_property_keys
        if partner_user_defined_property_keys is not None:
            request_body["partnerUserDefinedPropertyKeys"] = partner_user_defined_property_keys
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/platform/transfer-summaries/sheet-file",
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
        return response.text
