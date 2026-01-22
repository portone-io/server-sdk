from __future__ import annotations
import httpx
import json
from httpx import AsyncClient, Client as SyncClient
from ..._user_agent import USER_AGENT
from typing import Optional
from ..errors import ForbiddenError, InvalidRequestError, UnauthorizedError, UnknownError
from ..common.forbidden_error import _deserialize_forbidden_error
from ..common.invalid_request_error import _deserialize_invalid_request_error
from ..common.unauthorized_error import _deserialize_unauthorized_error
from ..common.date_range import DateRange, _deserialize_date_range, _serialize_date_range
from ..reconciliation.get_payment_reconciliation_settlement_vat_report_response import GetPaymentReconciliationSettlementVatReportResponse, _deserialize_get_payment_reconciliation_settlement_vat_report_response, _serialize_get_payment_reconciliation_settlement_vat_report_response
from ..reconciliation.get_payment_reconciliation_transaction_vat_report_response import GetPaymentReconciliationTransactionVatReportResponse, _deserialize_get_payment_reconciliation_transaction_vat_report_response, _serialize_get_payment_reconciliation_transaction_vat_report_response
from ..reconciliation.payment_reconciliation_settlement_summary_filter_input import PaymentReconciliationSettlementSummaryFilterInput, _deserialize_payment_reconciliation_settlement_summary_filter_input, _serialize_payment_reconciliation_settlement_summary_filter_input
from ..reconciliation.payment_reconciliation_transaction_summary_filter_input import PaymentReconciliationTransactionSummaryFilterInput, _deserialize_payment_reconciliation_transaction_summary_filter_input, _serialize_payment_reconciliation_transaction_summary_filter_input
from urllib.parse import quote
class ReconciliationClient:
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
    def get_payment_reconciliation_settlement_vat_report(
        self,
        *,
        date_range: DateRange,
        filter: Optional[PaymentReconciliationSettlementSummaryFilterInput] = None,
    ) -> GetPaymentReconciliationSettlementVatReportResponse:
        """정산일 기준 부가세 내역 조회

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            date_range (DateRange):
                정산일 범위
            filter (PaymentReconciliationSettlementSummaryFilterInput, optional):



        Raises:
            GetPaymentReconciliationSettlementVatReportError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["dateRange"] = _serialize_date_range(date_range)
        if filter is not None:
            request_body["filter"] = _serialize_payment_reconciliation_settlement_summary_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/payment-reconciliations/settlements/vat-report",
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
        return _deserialize_get_payment_reconciliation_settlement_vat_report_response(response.json())
    async def get_payment_reconciliation_settlement_vat_report_async(
        self,
        *,
        date_range: DateRange,
        filter: Optional[PaymentReconciliationSettlementSummaryFilterInput] = None,
    ) -> GetPaymentReconciliationSettlementVatReportResponse:
        """정산일 기준 부가세 내역 조회

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            date_range (DateRange):
                정산일 범위
            filter (PaymentReconciliationSettlementSummaryFilterInput, optional):



        Raises:
            GetPaymentReconciliationSettlementVatReportError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["dateRange"] = _serialize_date_range(date_range)
        if filter is not None:
            request_body["filter"] = _serialize_payment_reconciliation_settlement_summary_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/payment-reconciliations/settlements/vat-report",
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
        return _deserialize_get_payment_reconciliation_settlement_vat_report_response(response.json())
    def get_payment_reconciliation_transaction_vat_report(
        self,
        *,
        date_range: DateRange,
        filter: Optional[PaymentReconciliationTransactionSummaryFilterInput] = None,
    ) -> GetPaymentReconciliationTransactionVatReportResponse:
        """거래일 기준 부가세 내역 조회

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            date_range (DateRange):
                거래일 범위
            filter (PaymentReconciliationTransactionSummaryFilterInput, optional):



        Raises:
            GetPaymentReconciliationTransactionVatReportError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["dateRange"] = _serialize_date_range(date_range)
        if filter is not None:
            request_body["filter"] = _serialize_payment_reconciliation_transaction_summary_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = self._sync_client.request(
            "GET",
            f"{self._base_url}/payment-reconciliations/transactions/vat-report",
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
        return _deserialize_get_payment_reconciliation_transaction_vat_report_response(response.json())
    async def get_payment_reconciliation_transaction_vat_report_async(
        self,
        *,
        date_range: DateRange,
        filter: Optional[PaymentReconciliationTransactionSummaryFilterInput] = None,
    ) -> GetPaymentReconciliationTransactionVatReportResponse:
        """거래일 기준 부가세 내역 조회

        Warning:
            실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.


        Args:
            date_range (DateRange):
                거래일 범위
            filter (PaymentReconciliationTransactionSummaryFilterInput, optional):



        Raises:
            GetPaymentReconciliationTransactionVatReportError: API 호출이 실패한 경우
            ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우
        """
        request_body = {}
        request_body["dateRange"] = _serialize_date_range(date_range)
        if filter is not None:
            request_body["filter"] = _serialize_payment_reconciliation_transaction_summary_filter_input(filter)
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._async_client.request(
            "GET",
            f"{self._base_url}/payment-reconciliations/transactions/vat-report",
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
        return _deserialize_get_payment_reconciliation_transaction_vat_report_response(response.json())
