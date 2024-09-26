export type * from "./AnalyticsAverageAmountChart"
export type * from "./AnalyticsAverageAmountChartStat"
export type * from "./AnalyticsAverageAmountChartSummary"
export type * from "./AnalyticsCancellationRate"
export type * from "./AnalyticsCardChart"
export type * from "./AnalyticsCardChartStat"
export type * from "./AnalyticsCardCompanyChart"
export type * from "./AnalyticsCardCompanyChartRemainderStat"
export type * from "./AnalyticsCardCompanyChartStat"
export type * from "./AnalyticsCardCompanyChartSummary"
export type * from "./AnalyticsEasyPayChart"
export type * from "./AnalyticsEasyPayChartStat"
export type * from "./AnalyticsEasyPayProviderChart"
export type * from "./AnalyticsEasyPayProviderChartRemainderStat"
export type * from "./AnalyticsEasyPayProviderChartStat"
export type * from "./AnalyticsEasyPayProviderChartSummary"
export type * from "./AnalyticsOverseasPaymentUsage"
export type * from "./AnalyticsPaymentChart"
export type * from "./AnalyticsPaymentChartInsight"
export type * from "./AnalyticsPaymentChartStat"
export type * from "./AnalyticsPaymentMethodChart"
export type * from "./AnalyticsPaymentMethodChartStat"
export type * from "./AnalyticsPaymentMethodTrendChart"
export type * from "./AnalyticsPaymentMethodTrendChartStat"
export type * from "./AnalyticsPaymentStatusByPaymentClientChart"
export type * from "./AnalyticsPaymentStatusByPaymentClientChartStat"
export type * from "./AnalyticsPaymentStatusByPaymentMethodChart"
export type * from "./AnalyticsPaymentStatusByPaymentMethodChartStat"
export type * from "./AnalyticsPaymentStatusByPgCompanyChart"
export type * from "./AnalyticsPaymentStatusByPgCompanyChartStat"
export type * from "./AnalyticsPaymentStatusChart"
export type * from "./AnalyticsPaymentStatusChartStat"
export type * from "./AnalyticsPgCompanyChart"
export type * from "./AnalyticsPgCompanyChartStat"
export type * from "./AnalyticsPgCompanyTrendChart"
export type * from "./AnalyticsPgCompanyTrendChartStat"
export type * from "./AnalyticsTimeGranularity"
export type * from "./AnalyticsTimeGranularityDay"
export type * from "./AnalyticsTimeGranularityHour"
export type * from "./AnalyticsTimeGranularityMinute"
export type * from "./AnalyticsTimeGranularityMonth"
export type * from "./AnalyticsTimeGranularityWeek"
export type * from "./CardCompany"
export type * from "./GetAnalyticsAverageAmountChartBody"
export type * from "./GetAnalyticsCancellationRateBody"
export type * from "./GetAnalyticsCancellationRateError"
export type * from "./GetAnalyticsCardChartBody"
export type * from "./GetAnalyticsCardChartError"
export type * from "./GetAnalyticsCardCompanyChartBody"
export type * from "./GetAnalyticsCardCompanyChartError"
export type * from "./GetAnalyticsEasyPayChartBody"
export type * from "./GetAnalyticsEasyPayChartError"
export type * from "./GetAnalyticsEasyPayProviderChartBody"
export type * from "./GetAnalyticsEasyPayProviderChartError"
export type * from "./GetAnalyticsOverseasPaymentUsageError"
export type * from "./GetAnalyticsPaymentChartBody"
export type * from "./GetAnalyticsPaymentChartError"
export type * from "./GetAnalyticsPaymentChartInsightBody"
export type * from "./GetAnalyticsPaymentChartInsightError"
export type * from "./GetAnalyticsPaymentMethodChartBody"
export type * from "./GetAnalyticsPaymentMethodTrendChartBody"
export type * from "./GetAnalyticsPaymentStatusByPaymentClientChartBody"
export type * from "./GetAnalyticsPaymentStatusByPaymentMethodChartBody"
export type * from "./GetAnalyticsPaymentStatusByPgCompanyChartBody"
export type * from "./GetAnalyticsPaymentStatusChartBody"
export type * from "./GetAnalyticsPgCompanyChartBody"
export type * from "./GetAnalyticsPgCompanyTrendChartBody"
export type * from "./GetAverageAmountChartError"
export type * from "./GetPaymentMethodChartError"
export type * from "./GetPaymentMethodTrendChartError"
export type * from "./GetPaymentStatusByPaymentClientChartError"
export type * from "./GetPaymentStatusByPaymentMethodChartError"
export type * from "./GetPaymentStatusByPgCompanyChartError"
export type * from "./GetPaymentStatusChartError"
export type * from "./GetPgCompanyChartError"
export type * from "./GetPgCompanyTrendChartError"
import type { AnalyticsAverageAmountChart } from "#generated/analytics/AnalyticsAverageAmountChart"
import type { AnalyticsCancellationRate } from "#generated/analytics/AnalyticsCancellationRate"
import type { AnalyticsCardChart } from "#generated/analytics/AnalyticsCardChart"
import type { AnalyticsCardCompanyChart } from "#generated/analytics/AnalyticsCardCompanyChart"
import type { AnalyticsEasyPayChart } from "#generated/analytics/AnalyticsEasyPayChart"
import type { AnalyticsEasyPayProviderChart } from "#generated/analytics/AnalyticsEasyPayProviderChart"
import type { AnalyticsOverseasPaymentUsage } from "#generated/analytics/AnalyticsOverseasPaymentUsage"
import type { AnalyticsPaymentChart } from "#generated/analytics/AnalyticsPaymentChart"
import type { AnalyticsPaymentChartInsight } from "#generated/analytics/AnalyticsPaymentChartInsight"
import type { AnalyticsPaymentMethodChart } from "#generated/analytics/AnalyticsPaymentMethodChart"
import type { AnalyticsPaymentMethodTrendChart } from "#generated/analytics/AnalyticsPaymentMethodTrendChart"
import type { AnalyticsPaymentStatusByPaymentClientChart } from "#generated/analytics/AnalyticsPaymentStatusByPaymentClientChart"
import type { AnalyticsPaymentStatusByPaymentMethodChart } from "#generated/analytics/AnalyticsPaymentStatusByPaymentMethodChart"
import type { AnalyticsPaymentStatusByPgCompanyChart } from "#generated/analytics/AnalyticsPaymentStatusByPgCompanyChart"
import type { AnalyticsPaymentStatusChart } from "#generated/analytics/AnalyticsPaymentStatusChart"
import type { AnalyticsPgCompanyChart } from "#generated/analytics/AnalyticsPgCompanyChart"
import type { AnalyticsPgCompanyTrendChart } from "#generated/analytics/AnalyticsPgCompanyTrendChart"
import type { AnalyticsTimeGranularity } from "#generated/analytics/AnalyticsTimeGranularity"
import type { CardCompany } from "#generated/analytics/CardCompany"
import type { Currency } from "#generated/common/Currency"
import type { EasyPayProvider } from "#generated/common/EasyPayProvider"
import type { PgCompany } from "#generated/common/PgCompany"

export type Operations = {
	/**
	 * 고객사의 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsPaymentChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<AnalyticsPaymentChart>
	/**
	 * 고객사의 결제 현황 인사이트를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsPaymentChartInsight: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 타임존 시간 오프셋
		 *
		 * 입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.
		 * (int32)
		 */
		timezoneHourOffset: number,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<AnalyticsPaymentChartInsight>
	/**
	 * 고객사의 평균 거래액 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAverageAmountChart: (
		/**
		 * 조회할 평균 거래액 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 평균 거래액 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 평균 거래액 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsAverageAmountChart>
	/**
	 * 고객사의 결제수단 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentMethodChart: (
		/**
		 * 조회할 결제수단 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<AnalyticsPaymentMethodChart>
	/**
	 * 고객사의 결제수단 트렌드를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentMethodTrendChart: (
		/**
		 * 조회할 결제수단 트렌드의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 트렌드의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제수단 트렌드 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsPaymentMethodTrendChart>
	/**
	 * 고객사의 카드결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCardChart: (
		/**
		 * 조회할 카드결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsCardChart>
	/**
	 * 고객사의 카드사별 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCardCompanyChart: (
		/**
		 * 조회할 카드사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 카드사 */
		cardCompanies: CardCompany[],
		/** 나머지 집계에 포함되지 않을 카드사 */
		excludesFromRemainders: CardCompany[],
	) => Promise<AnalyticsCardCompanyChart>
	/**
	 * 고객사의 간편결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsEasyPayChart: (
		/**
		 * 조회할 간편결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
	) => Promise<AnalyticsEasyPayChart>
	/**
	 * 고객사의 간편결제사별 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsEasyPayProviderChart: (
		/**
		 * 조회할 간편결제사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 간편결제사 */
		easyPayProviders: EasyPayProvider[],
		/** 나머지 집계에 포함되지 않을 간편결제사 */
		excludesFromRemainders: EasyPayProvider[],
	) => Promise<AnalyticsEasyPayProviderChart>
	/**
	 * 고객사의 결제대행사 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPgCompanyChart: (
		/**
		 * 조회할 결제대행사 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<AnalyticsPgCompanyChart>
	/**
	 * 고객사의 결제대행사별 거래 추이를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPgCompanyTrendChart: (
		/**
		 * 조회할 결제대행사별 거래 추이의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사별 거래 추이의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제대행사별 거래 추이 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: AnalyticsTimeGranularity,
		/** 조회할 결제대행사 */
		pgCompanies: PgCompany[],
	) => Promise<AnalyticsPgCompanyTrendChart>
	/**
	 * 고객사의 해외 결제 사용 여부를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsOverseasPaymentUsage: (
	) => Promise<AnalyticsOverseasPaymentUsage>
	/**
	 * 고객사의 환불율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCancellationRate: (
		/**
		 * 환불율 조회 기간의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 환불율 조회 기간의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsCancellationRate>
	/**
	 * 고객사의 결제상태 이력 집계를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusChart>
	/**
	 * 고객사의 결제수단별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPaymentMethodChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPaymentMethodChart>
	/**
	 * 고객사의 PG사별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPgCompanyChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPgCompanyChart>
	/**
	 * 고객사의 결제환경별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPaymentClientChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Currency,
	) => Promise<AnalyticsPaymentStatusByPaymentClientChart>
}
