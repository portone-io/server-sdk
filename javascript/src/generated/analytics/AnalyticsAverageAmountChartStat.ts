/** 특정 시점의 건별 평균 거래액, 고객 당 평균 거래액을 나타냅니다. */
export type AnalyticsAverageAmountChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/**
	 * 건별 평균 거래액
	 * (int64)
	 */
	paymentAverageAmount: number
	/**
	 * 고객 당 평균 거래액
	 * (int64)
	 */
	customerAverageAmount: number
}
