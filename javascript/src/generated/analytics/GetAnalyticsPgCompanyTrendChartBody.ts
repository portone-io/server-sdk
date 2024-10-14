import type { AnalyticsTimeGranularity } from "#generated/analytics/AnalyticsTimeGranularity"
import type { Currency } from "#generated/common/Currency"
import type { PgCompany } from "#generated/common/PgCompany"

/** 고객사의 결제대행사별 거래 추이 조회를 위한 입력 정보 */
export type GetAnalyticsPgCompanyTrendChartBody = {
	/**
	 * 조회할 결제대행사별 거래 추이의 시작 시간
	 * (RFC 3339 date-time)
	 */
	from: string
	/**
	 * 조회할 결제대행사별 거래 추이의 끝 시간
	 * (RFC 3339 date-time)
	 */
	until: string
	/**
	 * 조회할 결제 통화
	 *
	 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
	 */
	currency: Currency
	/**
	 * 결제취소건 제외 여부
	 *
	 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
	 */
	excludeCancelled: boolean
	/**
	 * 결제 결제대행사별 거래 추이 조회 단위
	 *
	 * 시간별, 월별 단위만 지원됩니다.
	 */
	timeGranularity: AnalyticsTimeGranularity
	/** 조회할 결제대행사 */
	pgCompanies: PgCompany[]
}