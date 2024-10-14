from __future__ import annotations
import httpx
import json
from httpx import AsyncClient
from typing import Optional
from portone_server_sdk._generated.analytics.analytics_average_amount_chart import AnalyticsAverageAmountChart, _deserialize_analytics_average_amount_chart, _serialize_analytics_average_amount_chart
from portone_server_sdk._generated.analytics.analytics_cancellation_rate import AnalyticsCancellationRate, _deserialize_analytics_cancellation_rate, _serialize_analytics_cancellation_rate
from portone_server_sdk._generated.analytics.analytics_card_chart import AnalyticsCardChart, _deserialize_analytics_card_chart, _serialize_analytics_card_chart
from portone_server_sdk._generated.analytics.analytics_card_company_chart import AnalyticsCardCompanyChart, _deserialize_analytics_card_company_chart, _serialize_analytics_card_company_chart
from portone_server_sdk._generated.analytics.analytics_easy_pay_chart import AnalyticsEasyPayChart, _deserialize_analytics_easy_pay_chart, _serialize_analytics_easy_pay_chart
from portone_server_sdk._generated.analytics.analytics_easy_pay_provider_chart import AnalyticsEasyPayProviderChart, _deserialize_analytics_easy_pay_provider_chart, _serialize_analytics_easy_pay_provider_chart
from portone_server_sdk._generated.analytics.analytics_overseas_payment_usage import AnalyticsOverseasPaymentUsage, _deserialize_analytics_overseas_payment_usage, _serialize_analytics_overseas_payment_usage
from portone_server_sdk._generated.analytics.analytics_payment_chart import AnalyticsPaymentChart, _deserialize_analytics_payment_chart, _serialize_analytics_payment_chart
from portone_server_sdk._generated.analytics.analytics_payment_chart_insight import AnalyticsPaymentChartInsight, _deserialize_analytics_payment_chart_insight, _serialize_analytics_payment_chart_insight
from portone_server_sdk._generated.analytics.analytics_payment_method_chart import AnalyticsPaymentMethodChart, _deserialize_analytics_payment_method_chart, _serialize_analytics_payment_method_chart
from portone_server_sdk._generated.analytics.analytics_payment_method_trend_chart import AnalyticsPaymentMethodTrendChart, _deserialize_analytics_payment_method_trend_chart, _serialize_analytics_payment_method_trend_chart
from portone_server_sdk._generated.analytics.analytics_payment_status_by_payment_client_chart import AnalyticsPaymentStatusByPaymentClientChart, _deserialize_analytics_payment_status_by_payment_client_chart, _serialize_analytics_payment_status_by_payment_client_chart
from portone_server_sdk._generated.analytics.analytics_payment_status_by_payment_method_chart import AnalyticsPaymentStatusByPaymentMethodChart, _deserialize_analytics_payment_status_by_payment_method_chart, _serialize_analytics_payment_status_by_payment_method_chart
from portone_server_sdk._generated.analytics.analytics_payment_status_by_pg_company_chart import AnalyticsPaymentStatusByPgCompanyChart, _deserialize_analytics_payment_status_by_pg_company_chart, _serialize_analytics_payment_status_by_pg_company_chart
from portone_server_sdk._generated.analytics.analytics_payment_status_chart import AnalyticsPaymentStatusChart, _deserialize_analytics_payment_status_chart, _serialize_analytics_payment_status_chart
from portone_server_sdk._generated.analytics.analytics_pg_company_chart import AnalyticsPgCompanyChart, _deserialize_analytics_pg_company_chart, _serialize_analytics_pg_company_chart
from portone_server_sdk._generated.analytics.analytics_pg_company_trend_chart import AnalyticsPgCompanyTrendChart, _deserialize_analytics_pg_company_trend_chart, _serialize_analytics_pg_company_trend_chart
from portone_server_sdk._generated.analytics.analytics_time_granularity import AnalyticsTimeGranularity, _deserialize_analytics_time_granularity, _serialize_analytics_time_granularity
from portone_server_sdk._generated.analytics.card_company import CardCompany, _deserialize_card_company, _serialize_card_company
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated import errors
class AnalyticsClient:
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
    def get_analytics_payment_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: Optional[bool] = None,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsPaymentChart:
        """고객사의 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool, optional):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        if exclude_cancelled is not None:
            request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment",
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
        return _deserialize_analytics_payment_chart(response.json())
    async def get_analytics_payment_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: Optional[bool] = None,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsPaymentChart:
        """고객사의 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool, optional):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        if exclude_cancelled is not None:
            request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment",
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
        return _deserialize_analytics_payment_chart(response.json())
    def get_analytics_payment_chart_insight(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: Optional[bool] = None,
        timezone_hour_offset: int,
    ) -> AnalyticsPaymentChartInsight:
        """고객사의 결제 현황 인사이트를 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool, optional):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            timezone_hour_offset (int):
                타임존 시간 오프셋

                입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        if exclude_cancelled is not None:
            request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timezoneHourOffset"] = timezone_hour_offset,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-insight",
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
        return _deserialize_analytics_payment_chart_insight(response.json())
    async def get_analytics_payment_chart_insight_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: Optional[bool] = None,
        timezone_hour_offset: int,
    ) -> AnalyticsPaymentChartInsight:
        """고객사의 결제 현황 인사이트를 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool, optional):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            timezone_hour_offset (int):
                타임존 시간 오프셋

                입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        if exclude_cancelled is not None:
            request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timezoneHourOffset"] = timezone_hour_offset,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-insight",
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
        return _deserialize_analytics_payment_chart_insight(response.json())
    def get_average_amount_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsAverageAmountChart:
        """고객사의 평균 거래액 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 평균 거래액 현황의 시작 시간
            until (str):
                조회할 평균 거래액 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                평균 거래액 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/average-amount",
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
        return _deserialize_analytics_average_amount_chart(response.json())
    async def get_average_amount_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsAverageAmountChart:
        """고객사의 평균 거래액 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 평균 거래액 현황의 시작 시간
            until (str):
                조회할 평균 거래액 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                평균 거래액 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/average-amount",
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
        return _deserialize_analytics_average_amount_chart(response.json())
    def get_payment_method_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
    ) -> AnalyticsPaymentMethodChart:
        """고객사의 결제수단 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제수단 현황의 시작 시간
            until (str):
                조회할 결제수단 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-method",
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
        return _deserialize_analytics_payment_method_chart(response.json())
    async def get_payment_method_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
    ) -> AnalyticsPaymentMethodChart:
        """고객사의 결제수단 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제수단 현황의 시작 시간
            until (str):
                조회할 결제수단 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-method",
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
        return _deserialize_analytics_payment_method_chart(response.json())
    def get_payment_method_trend_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsPaymentMethodTrendChart:
        """고객사의 결제수단 트렌드를 조회합니다.

        Args:
            from_ (str):
                조회할 결제수단 트렌드의 시작 시간
            until (str):
                조회할 결제수단 트렌드의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 결제수단 트렌드 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-method-trend",
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
        return _deserialize_analytics_payment_method_trend_chart(response.json())
    async def get_payment_method_trend_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsPaymentMethodTrendChart:
        """고객사의 결제수단 트렌드를 조회합니다.

        Args:
            from_ (str):
                조회할 결제수단 트렌드의 시작 시간
            until (str):
                조회할 결제수단 트렌드의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 결제수단 트렌드 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-method-trend",
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
        return _deserialize_analytics_payment_method_trend_chart(response.json())
    def get_analytics_card_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsCardChart:
        """고객사의 카드결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 카드결제 현황의 시작 시간
            until (str):
                조회할 카드결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                카드결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/card",
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
        return _deserialize_analytics_card_chart(response.json())
    async def get_analytics_card_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsCardChart:
        """고객사의 카드결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 카드결제 현황의 시작 시간
            until (str):
                조회할 카드결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                카드결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/card",
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
        return _deserialize_analytics_card_chart(response.json())
    def get_analytics_card_company_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        card_companies: list[CardCompany],
        excludes_from_remainders: list[CardCompany],
    ) -> AnalyticsCardCompanyChart:
        """고객사의 카드사별 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 카드사별 결제 현황의 시작 시간
            until (str):
                조회할 카드사별 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                카드사별 결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.
            card_companies (list[CardCompany]):
                조회할 카드사
            excludes_from_remainders (list[CardCompany]):
                나머지 집계에 포함되지 않을 카드사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["cardCompanies"] = card_companies,
        request_body["excludesFromRemainders"] = excludes_from_remainders,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/card-company",
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
        return _deserialize_analytics_card_company_chart(response.json())
    async def get_analytics_card_company_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        card_companies: list[CardCompany],
        excludes_from_remainders: list[CardCompany],
    ) -> AnalyticsCardCompanyChart:
        """고객사의 카드사별 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 카드사별 결제 현황의 시작 시간
            until (str):
                조회할 카드사별 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                카드사별 결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.
            card_companies (list[CardCompany]):
                조회할 카드사
            excludes_from_remainders (list[CardCompany]):
                나머지 집계에 포함되지 않을 카드사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["cardCompanies"] = card_companies,
        request_body["excludesFromRemainders"] = excludes_from_remainders,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/card-company",
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
        return _deserialize_analytics_card_company_chart(response.json())
    def get_analytics_easy_pay_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsEasyPayChart:
        """고객사의 간편결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 간편결제 현황의 시작 시간
            until (str):
                조회할 간편결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                간편결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/easy-pay",
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
        return _deserialize_analytics_easy_pay_chart(response.json())
    async def get_analytics_easy_pay_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
    ) -> AnalyticsEasyPayChart:
        """고객사의 간편결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 간편결제 현황의 시작 시간
            until (str):
                조회할 간편결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                간편결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/easy-pay",
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
        return _deserialize_analytics_easy_pay_chart(response.json())
    def get_analytics_easy_pay_provider_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        easy_pay_providers: list[EasyPayProvider],
        excludes_from_remainders: list[EasyPayProvider],
    ) -> AnalyticsEasyPayProviderChart:
        """고객사의 간편결제사별 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 간편결제사별 결제 현황의 시작 시간
            until (str):
                조회할 간편결제사별 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                간편결제사별 결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.
            easy_pay_providers (list[EasyPayProvider]):
                조회할 간편결제사
            excludes_from_remainders (list[EasyPayProvider]):
                나머지 집계에 포함되지 않을 간편결제사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["easyPayProviders"] = easy_pay_providers,
        request_body["excludesFromRemainders"] = excludes_from_remainders,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/easy-pay-provider",
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
        return _deserialize_analytics_easy_pay_provider_chart(response.json())
    async def get_analytics_easy_pay_provider_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        easy_pay_providers: list[EasyPayProvider],
        excludes_from_remainders: list[EasyPayProvider],
    ) -> AnalyticsEasyPayProviderChart:
        """고객사의 간편결제사별 결제 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 간편결제사별 결제 현황의 시작 시간
            until (str):
                조회할 간편결제사별 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                간편결제사별 결제 현황 조회 단위

                시간별, 월별 단위만 지원됩니다.
            easy_pay_providers (list[EasyPayProvider]):
                조회할 간편결제사
            excludes_from_remainders (list[EasyPayProvider]):
                나머지 집계에 포함되지 않을 간편결제사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["easyPayProviders"] = easy_pay_providers,
        request_body["excludesFromRemainders"] = excludes_from_remainders,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/easy-pay-provider",
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
        return _deserialize_analytics_easy_pay_provider_chart(response.json())
    def get_pg_company_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
    ) -> AnalyticsPgCompanyChart:
        """고객사의 결제대행사 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제대행사 현황의 시작 시간
            until (str):
                조회할 결제대행사 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/pg-company",
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
        return _deserialize_analytics_pg_company_chart(response.json())
    async def get_pg_company_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
    ) -> AnalyticsPgCompanyChart:
        """고객사의 결제대행사 현황을 조회합니다.

        Args:
            from_ (str):
                조회할 결제대행사 현황의 시작 시간
            until (str):
                조회할 결제대행사 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/pg-company",
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
        return _deserialize_analytics_pg_company_chart(response.json())
    def get_pg_company_trend_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        pg_companies: list[PgCompany],
    ) -> AnalyticsPgCompanyTrendChart:
        """고객사의 결제대행사별 거래 추이를 조회합니다.

        Args:
            from_ (str):
                조회할 결제대행사별 거래 추이의 시작 시간
            until (str):
                조회할 결제대행사별 거래 추이의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 결제대행사별 거래 추이 조회 단위

                시간별, 월별 단위만 지원됩니다.
            pg_companies (list[PgCompany]):
                조회할 결제대행사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["pgCompanies"] = pg_companies,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/pg-company-trend",
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
        return _deserialize_analytics_pg_company_trend_chart(response.json())
    async def get_pg_company_trend_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
        exclude_cancelled: bool,
        time_granularity: AnalyticsTimeGranularity,
        pg_companies: list[PgCompany],
    ) -> AnalyticsPgCompanyTrendChart:
        """고객사의 결제대행사별 거래 추이를 조회합니다.

        Args:
            from_ (str):
                조회할 결제대행사별 거래 추이의 시작 시간
            until (str):
                조회할 결제대행사별 거래 추이의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
            exclude_cancelled (bool):
                결제취소건 제외 여부

                true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
            time_granularity (AnalyticsTimeGranularity):
                결제 결제대행사별 거래 추이 조회 단위

                시간별, 월별 단위만 지원됩니다.
            pg_companies (list[PgCompany]):
                조회할 결제대행사


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        request_body["excludeCancelled"] = exclude_cancelled,
        request_body["timeGranularity"] = _serialize_analytics_time_granularity(time_granularity),
        request_body["pgCompanies"] = pg_companies,
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/pg-company-trend",
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
        return _deserialize_analytics_pg_company_trend_chart(response.json())
    def get_analytics_overseas_payment_usage(
        self,
    ) -> AnalyticsOverseasPaymentUsage:
        """고객사의 해외 결제 사용 여부를 조회합니다.

        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/overseas-payment-usage",
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
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_analytics_overseas_payment_usage(response.json())
    async def get_analytics_overseas_payment_usage_async(
        self,
    ) -> AnalyticsOverseasPaymentUsage:
        """고객사의 해외 결제 사용 여부를 조회합니다.

        Raises:
            ForbiddenError: 요청이 거절된 경우
                요청이 거절된 경우
            UnauthorizedError: 인증 정보가 올바르지 않은 경우
                인증 정보가 올바르지 않은 경우
            UnknownError: API 응답이 알 수 없는 형식인 경우
        """
        query = []
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/overseas-payment-usage",
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
            if error_type == "UNAUTHORIZED":
                raise errors.UnauthorizedError(_deserialize_unauthorized_error(error_response))
            else:
                raise errors.UnknownError(error_response)
        return _deserialize_analytics_overseas_payment_usage(response.json())
    def get_analytics_cancellation_rate(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsCancellationRate:
        """고객사의 환불율을 조회합니다.

        Args:
            from_ (str):
                환불율 조회 기간의 시작 시간
            until (str):
                환불율 조회 기간의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/cancellation-rate",
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
        return _deserialize_analytics_cancellation_rate(response.json())
    async def get_analytics_cancellation_rate_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsCancellationRate:
        """고객사의 환불율을 조회합니다.

        Args:
            from_ (str):
                환불율 조회 기간의 시작 시간
            until (str):
                환불율 조회 기간의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/cancellation-rate",
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
        return _deserialize_analytics_cancellation_rate(response.json())
    def get_payment_status_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusChart:
        """고객사의 결제상태 이력 집계를 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status",
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
        return _deserialize_analytics_payment_status_chart(response.json())
    async def get_payment_status_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusChart:
        """고객사의 결제상태 이력 집계를 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status",
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
        return _deserialize_analytics_payment_status_chart(response.json())
    def get_payment_status_by_payment_method_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPaymentMethodChart:
        """고객사의 결제수단별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-method",
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
        return _deserialize_analytics_payment_status_by_payment_method_chart(response.json())
    async def get_payment_status_by_payment_method_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPaymentMethodChart:
        """고객사의 결제수단별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-method",
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
        return _deserialize_analytics_payment_status_by_payment_method_chart(response.json())
    def get_payment_status_by_pg_company_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPgCompanyChart:
        """고객사의 PG사별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-pg-company",
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
        return _deserialize_analytics_payment_status_by_pg_company_chart(response.json())
    async def get_payment_status_by_pg_company_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPgCompanyChart:
        """고객사의 PG사별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-pg-company",
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
        return _deserialize_analytics_payment_status_by_pg_company_chart(response.json())
    def get_payment_status_by_payment_client_chart(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPaymentClientChart:
        """고객사의 결제환경별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = httpx.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-payment-client",
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
        return _deserialize_analytics_payment_status_by_payment_client_chart(response.json())
    async def get_payment_status_by_payment_client_chart_async(
        self,
        *,
        from_: str,
        until: str,
        currency: Currency,
    ) -> AnalyticsPaymentStatusByPaymentClientChart:
        """고객사의 결제환경별 결제전환율을 조회합니다.

        Args:
            from_ (str):
                조회할 결제 현황의 시작 시간
            until (str):
                조회할 결제 현황의 끝 시간
            currency (Currency):
                조회할 결제 통화

                입력된 통화로 발생한 결제내역만 응답에 포함됩니다.


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
        request_body["from"] = from_,
        request_body["until"] = until,
        request_body["currency"] = _serialize_currency(currency),
        query = []
        query.append(("requestBody", json.dumps(request_body)))
        response = await self._client.request(
            "GET",
            f"{self._base_url}/analytics/charts/payment-status/by-payment-client",
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
        return _deserialize_analytics_payment_status_by_payment_client_chart(response.json())
