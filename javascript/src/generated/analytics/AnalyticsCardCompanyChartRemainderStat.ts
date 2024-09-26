/** 특정 시점의 나머지 카드사들의 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsCardCompanyChartRemainderStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
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
