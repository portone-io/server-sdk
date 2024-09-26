/** 전체 구간의 건별 평균 거래액, 고객 당 평균 거래액을 나타냅니다. */
export type AnalyticsAverageAmountChartSummary = {
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
