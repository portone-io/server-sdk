import type { CardCompany } from "#generated/analytics/CardCompany"

/** 특정 시점의 카드사 별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsCardCompanyChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 카드사 */
	cardCompany: CardCompany
	/**
	 * 결제금액
	 * (int64)
	 */
	amount: number
	/**
	 * 결제 건수
	 * (int64)
	 */
	count: number
}
