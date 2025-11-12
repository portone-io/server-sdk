from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ...._user_agent import USER_AGENT
from typing import Optional
from ...errors import ForbiddenError, InvalidRequestError, PlatformAdditionalFeePoliciesNotFoundError, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCancelOrderTransfersExistsError, PlatformCancellableAmountExceededError, PlatformCancellableDiscountAmountExceededError, PlatformCancellableDiscountTaxFreeAmountExceededError, PlatformCancellableProductQuantityExceededError, PlatformCancellationAndPaymentTypeMismatchedError, PlatformCancellationNotFoundError, PlatformCannotSpecifyTransferError, PlatformContractNotFoundError, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCurrencyNotSupportedError, PlatformDiscountSharePoliciesNotFoundError, PlatformDiscountSharePolicyIdDuplicatedError, PlatformNotEnabledError, PlatformOrderDetailMismatchedError, PlatformOrderTransferAlreadyCancelledError, PlatformPartnerNotFoundError, PlatformPaymentNotFoundError, PlatformProductIdDuplicatedError, PlatformProductIdNotFoundError, PlatformSettlementAmountExceededError, PlatformSettlementCancelAmountExceededPortOneCancelError, PlatformSettlementDateEarlierThanSettlementStartDateError, PlatformSettlementParameterNotFoundError, PlatformSettlementPaymentAmountExceededPortOnePaymentError, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, PlatformTransferAlreadyExistsError, PlatformTransferDiscountSharePolicyNotFoundError, PlatformTransferNonDeletableStatusError, PlatformTransferNotFoundError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, UnknownError
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
from ...platform.transfer.platform_settlement_date_earlier_than_settlement_start_date_error import _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error
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
from ...platform.transfer.platform_user_defined_property_key_value import PlatformUserDefinedPropertyKeyValue, _deserialize_platform_user_defined_property_key_value, _serialize_platform_user_defined_property_key_value
from ...platform.transfer.transfer_parameters import TransferParameters, _deserialize_transfer_parameters, _serialize_transfer_parameters
from urllib.parse import quote
class TransferClient:
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
    def download_platform_transfer_sheet(
        self,
        *,
        test: Optional[bool] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
        fields: Optional[list[str]] = None,
    ) -> str:
        """정산 상세 내역 다운로드

        정산 상세 내역을 csv 파일로 다운로드 합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            filter (PlatformTransferFilterInput, optional):
                컬럼 키 목록

                - TRANSFER_MEMO:  메모
                - TRANSFER_TYPE: 정산 유형
                - TRANSFER_STATUS:  상태
                - TRANSFER_ID: 정산 아이디
                - TRANSFER_SETTLEMENT_DATE:  정산일
                - TRANSFER_SETTLEMENT_AMOUNT: 정산 금액
                - TRANSFER_SETTLEMENT_TAX_FREE_AMOUNT: 정산 면세액
                - TRANSFER_SETTLEMENT_CURRENCY: 정산 통화
                - TRANSFER_SETTLEMENT_START_DATE: 정산 시작일
                - TRANSFER_ORDER_NAME:  주문명
                - TRANSFER_ORDER_AMOUNT: 주문 금액
                - TRANSFER_ORDER_TAX_FREE_AMOUNT: 주문 면세액
                - TRANSFER_PAYMENT_ID: 주문 번호
                - TRANSFER_PAYMENT_METHOD: 결제 수단
                - TRANSFER_PAYMENT_AMOUNT: 결제 금액
                - TRANSFER_PAYMENT_SUPPLY_AMOUNT: 결제 공급가액
                - TRANSFER_PAYMENT_VAT_AMOUNT: 결제 부가세액
                - TRANSFER_PAYMENT_TAX_FREE_AMOUNT: 결제 면세액
                - TRANSFER_PAYMENT_VAT_BURDEN_AMOUNT: 결제 부가세 부담금
                - TRANSFER_PLATFORM_FEE:  중개수수료
                - TRANSFER_PLATFORM_FEE_VAT: 중개수수료 부가세 부담금
                - TRANSFER_CONTRACT_ID: 계약 아이디
                - TRANSFER_CONTRACT_NAME: 계약 이름
                - TRANSFER_DISCOUNT_AMOUNT: 할인 금액
                - TRANSFER_DISCOUNT_TAX_FREE_AMOUNT: 할인 면세액
                - TRANSFER_DISCOUNT_SHARE_AMOUNT: 할인 분담금
                - TRANSFER_DISCOUNT_SHARE_TAX_FREE_AMOUNT: 할인 면세 분담금
                - TRANSFER_ADDITIONAL_FEE:  추가수수료
                - TRANSFER_ADDITIONAL_FEE_VAT: 추가수수료 부가세 부담금
                - TRANSFER_{UserDefinedProperty.Key}
                - FORMULA_{UserDefinedFormula.Key}
                - PARTNER_* : 파트너 컬럼 키 사용 가능(w/o PARTNER_STATUS_UPDATED_AT)
            fields (list[str], optional):



        Raises:
            DownloadPlatformTransferSheetError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        if fields is not None:
            request_body["fields"] = fields
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
        fields: Optional[list[str]] = None,
    ) -> str:
        """정산 상세 내역 다운로드

        정산 상세 내역을 csv 파일로 다운로드 합니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            filter (PlatformTransferFilterInput, optional):
                컬럼 키 목록

                - TRANSFER_MEMO:  메모
                - TRANSFER_TYPE: 정산 유형
                - TRANSFER_STATUS:  상태
                - TRANSFER_ID: 정산 아이디
                - TRANSFER_SETTLEMENT_DATE:  정산일
                - TRANSFER_SETTLEMENT_AMOUNT: 정산 금액
                - TRANSFER_SETTLEMENT_TAX_FREE_AMOUNT: 정산 면세액
                - TRANSFER_SETTLEMENT_CURRENCY: 정산 통화
                - TRANSFER_SETTLEMENT_START_DATE: 정산 시작일
                - TRANSFER_ORDER_NAME:  주문명
                - TRANSFER_ORDER_AMOUNT: 주문 금액
                - TRANSFER_ORDER_TAX_FREE_AMOUNT: 주문 면세액
                - TRANSFER_PAYMENT_ID: 주문 번호
                - TRANSFER_PAYMENT_METHOD: 결제 수단
                - TRANSFER_PAYMENT_AMOUNT: 결제 금액
                - TRANSFER_PAYMENT_SUPPLY_AMOUNT: 결제 공급가액
                - TRANSFER_PAYMENT_VAT_AMOUNT: 결제 부가세액
                - TRANSFER_PAYMENT_TAX_FREE_AMOUNT: 결제 면세액
                - TRANSFER_PAYMENT_VAT_BURDEN_AMOUNT: 결제 부가세 부담금
                - TRANSFER_PLATFORM_FEE:  중개수수료
                - TRANSFER_PLATFORM_FEE_VAT: 중개수수료 부가세 부담금
                - TRANSFER_CONTRACT_ID: 계약 아이디
                - TRANSFER_CONTRACT_NAME: 계약 이름
                - TRANSFER_DISCOUNT_AMOUNT: 할인 금액
                - TRANSFER_DISCOUNT_TAX_FREE_AMOUNT: 할인 면세액
                - TRANSFER_DISCOUNT_SHARE_AMOUNT: 할인 분담금
                - TRANSFER_DISCOUNT_SHARE_TAX_FREE_AMOUNT: 할인 면세 분담금
                - TRANSFER_ADDITIONAL_FEE:  추가수수료
                - TRANSFER_ADDITIONAL_FEE_VAT: 추가수수료 부가세 부담금
                - TRANSFER_{UserDefinedProperty.Key}
                - FORMULA_{UserDefinedFormula.Key}
                - PARTNER_* : 파트너 컬럼 키 사용 가능(w/o PARTNER_STATUS_UPDATED_AT)
            fields (list[str], optional):



        Raises:
            DownloadPlatformTransferSheetError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        if filter is not None:
            request_body["filter"] = _serialize_platform_transfer_filter_input(filter)
        if fields is not None:
            request_body["fields"] = fields
        query = []
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
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
    def get_platform_transfer_summaries(
        self,
        *,
        test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
    ) -> GetPlatformTransferSummariesResponse:
        """정산건 다건 조회

        성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        page: Optional[PageInput] = None,
        filter: Optional[PlatformTransferFilterInput] = None,
    ) -> GetPlatformTransferSummariesResponse:
        """정산건 다건 조회

        성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if test is not None:
            query.append(("test", test))
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
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
    def create_platform_manual_transfer(
        self,
        *,
        test: Optional[bool] = None,
        partner_id: str,
        memo: Optional[str] = None,
        settlement_amount: int,
        settlement_tax_free_amount: Optional[int] = None,
        settlement_date: str,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateManualTransferResponse:
        """수기 정산건 생성

        성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            partner_id (str):
                파트너 아이디
            memo (str, optional):
                메모
            settlement_amount (int):
                정산 금액
            settlement_tax_free_amount (int, optional):
                정산 면세 금액
            settlement_date (str):
                정산 일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if settlement_tax_free_amount is not None:
            request_body["settlementTaxFreeAmount"] = settlement_tax_free_amount
        request_body["settlementDate"] = settlement_date
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
        partner_id: str,
        memo: Optional[str] = None,
        settlement_amount: int,
        settlement_tax_free_amount: Optional[int] = None,
        settlement_date: str,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateManualTransferResponse:
        """수기 정산건 생성

        성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
            partner_id (str):
                파트너 아이디
            memo (str, optional):
                메모
            settlement_amount (int):
                정산 금액
            settlement_tax_free_amount (int, optional):
                정산 면세 금액
            settlement_date (str):
                정산 일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if settlement_tax_free_amount is not None:
            request_body["settlementTaxFreeAmount"] = settlement_tax_free_amount
        request_body["settlementDate"] = settlement_date
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
    def create_platform_order_cancel_transfer(
        self,
        *,
        test: Optional[bool] = None,
        partner_id: Optional[str] = None,
        payment_id: Optional[str] = None,
        transfer_id: Optional[str] = None,
        cancellation_id: str,
        memo: Optional[str] = None,
        order_detail: Optional[CreatePlatformOrderCancelTransferBodyOrderDetail] = None,
        tax_free_amount: Optional[int] = None,
        discounts: list[CreatePlatformOrderCancelTransferBodyDiscount],
        settlement_start_date: Optional[str] = None,
        settlement_date: Optional[str] = None,
        external_cancellation_detail: Optional[CreatePlatformOrderCancelTransferBodyExternalCancellationDetail] = None,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderCancelTransferResponse:
        """주문 취소 정산건 생성

        성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
                (int64)
            discounts (list[CreatePlatformOrderCancelTransferBodyDiscount]):
                할인 정보
            settlement_start_date (str, optional):
                정산 시작일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            settlement_date (str, optional):
                정산일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            external_cancellation_detail (CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        request_body["discounts"] = [_serialize_create_platform_order_cancel_transfer_body_discount(item) for item in discounts]
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        if settlement_date is not None:
            request_body["settlementDate"] = settlement_date
        if external_cancellation_detail is not None:
            request_body["externalCancellationDetail"] = _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(external_cancellation_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
                error = _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementDateEarlierThanSettlementStartDateError(error)
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
        test: Optional[bool] = None,
        partner_id: Optional[str] = None,
        payment_id: Optional[str] = None,
        transfer_id: Optional[str] = None,
        cancellation_id: str,
        memo: Optional[str] = None,
        order_detail: Optional[CreatePlatformOrderCancelTransferBodyOrderDetail] = None,
        tax_free_amount: Optional[int] = None,
        discounts: list[CreatePlatformOrderCancelTransferBodyDiscount],
        settlement_start_date: Optional[str] = None,
        settlement_date: Optional[str] = None,
        external_cancellation_detail: Optional[CreatePlatformOrderCancelTransferBodyExternalCancellationDetail] = None,
        is_for_test: Optional[bool] = None,
        user_defined_properties: Optional[list[PlatformUserDefinedPropertyKeyValue]] = None,
    ) -> CreateOrderCancelTransferResponse:
        """주문 취소 정산건 생성

        성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.

        Args:
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
                (int64)
            discounts (list[CreatePlatformOrderCancelTransferBodyDiscount]):
                할인 정보
            settlement_start_date (str, optional):
                정산 시작일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            settlement_date (str, optional):
                정산일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            external_cancellation_detail (CreatePlatformOrderCancelTransferBodyExternalCancellationDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        request_body["discounts"] = [_serialize_create_platform_order_cancel_transfer_body_discount(item) for item in discounts]
        if settlement_start_date is not None:
            request_body["settlementStartDate"] = settlement_start_date
        if settlement_date is not None:
            request_body["settlementDate"] = settlement_date
        if external_cancellation_detail is not None:
            request_body["externalCancellationDetail"] = _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(external_cancellation_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
                error = _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementDateEarlierThanSettlementStartDateError(error)
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
    def create_platform_order_transfer(
        self,
        *,
        test: Optional[bool] = None,
        partner_id: str,
        contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        payment_id: str,
        order_detail: CreatePlatformOrderTransferBodyOrderDetail,
        tax_free_amount: Optional[int] = None,
        settlement_start_date: Optional[str] = None,
        settlement_date: Optional[str] = None,
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
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
                (int64)
            settlement_start_date (str, optional):
                정산 시작일

                기본값은 결제 일시 입니다.
                (yyyy-MM-dd)
            settlement_date (str, optional):
                정산일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            discounts (list[CreatePlatformOrderTransferBodyDiscount]):
                할인 정보
            additional_fees (list[CreatePlatformOrderTransferBodyAdditionalFee]):
                추가 수수료 정보
            external_payment_detail (CreatePlatformOrderTransferBodyExternalPaymentDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if settlement_date is not None:
            request_body["settlementDate"] = settlement_date
        request_body["discounts"] = [_serialize_create_platform_order_transfer_body_discount(item) for item in discounts]
        request_body["additionalFees"] = [_serialize_create_platform_order_transfer_body_additional_fee(item) for item in additional_fees]
        if external_payment_detail is not None:
            request_body["externalPaymentDetail"] = _serialize_create_platform_order_transfer_body_external_payment_detail(external_payment_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if parameters is not None:
            request_body["parameters"] = _serialize_transfer_parameters(parameters)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
                error = _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementDateEarlierThanSettlementStartDateError(error)
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
        test: Optional[bool] = None,
        partner_id: str,
        contract_id: Optional[str] = None,
        memo: Optional[str] = None,
        payment_id: str,
        order_detail: CreatePlatformOrderTransferBodyOrderDetail,
        tax_free_amount: Optional[int] = None,
        settlement_start_date: Optional[str] = None,
        settlement_date: Optional[str] = None,
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
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
                (int64)
            settlement_start_date (str, optional):
                정산 시작일

                기본값은 결제 일시 입니다.
                (yyyy-MM-dd)
            settlement_date (str, optional):
                정산일

                날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
                (yyyy-MM-dd)
            discounts (list[CreatePlatformOrderTransferBodyDiscount]):
                할인 정보
            additional_fees (list[CreatePlatformOrderTransferBodyAdditionalFee]):
                추가 수수료 정보
            external_payment_detail (CreatePlatformOrderTransferBodyExternalPaymentDetail, optional):
                외부 결제 상세 정보

                해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
            is_for_test (bool, optional):
                테스트 모드 여부

                Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
                Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
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
        if settlement_date is not None:
            request_body["settlementDate"] = settlement_date
        request_body["discounts"] = [_serialize_create_platform_order_transfer_body_discount(item) for item in discounts]
        request_body["additionalFees"] = [_serialize_create_platform_order_transfer_body_additional_fee(item) for item in additional_fees]
        if external_payment_detail is not None:
            request_body["externalPaymentDetail"] = _serialize_create_platform_order_transfer_body_external_payment_detail(external_payment_detail)
        if is_for_test is not None:
            request_body["isForTest"] = is_for_test
        if parameters is not None:
            request_body["parameters"] = _serialize_transfer_parameters(parameters)
        if user_defined_properties is not None:
            request_body["userDefinedProperties"] = [_serialize_platform_user_defined_property_key_value(item) for item in user_defined_properties]
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
                error = _deserialize_platform_settlement_date_earlier_than_settlement_start_date_error(error_response)
            except Exception:
                pass
            if error is not None:
                raise PlatformSettlementDateEarlierThanSettlementStartDateError(error)
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
    def get_platform_transfer(
        self,
        *,
        id: str,
        test: Optional[bool] = None,
    ) -> PlatformTransfer:
        """정산건 조회

        정산건을 조회합니다.

        Args:
            id (str):
                조회하고 싶은 정산건 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> PlatformTransfer:
        """정산건 조회

        정산건을 조회합니다.

        Args:
            id (str):
                조회하고 싶은 정산건 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            GetPlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
        test: Optional[bool] = None,
    ) -> DeletePlatformTransferResponse:
        """정산건 삭제

        scheduled, in_process 상태의 정산건만 삭제가능합니다.

        Args:
            id (str):
                정산건 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            DeletePlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = self._sync_client.request(
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
        test: Optional[bool] = None,
    ) -> DeletePlatformTransferResponse:
        """정산건 삭제

        scheduled, in_process 상태의 정산건만 삭제가능합니다.

        Args:
            id (str):
                정산건 아이디
            test (bool, optional):
                테스트 모드 여부

                테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.


        Raises:
            DeletePlatformTransferError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        query = []
        if test is not None:
            query.append(("test", test))
        response = await self._async_client.request(
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
