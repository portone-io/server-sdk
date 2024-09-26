/** 결제금액, 결제 건수의 총합을 나타냅니다. */
export type AnalyticsEasyPayProviderChartSummary = {
	/**
	 * 결제금액의 합
	 * (int64)
	 */
	totalAmount: number
	/**
	 * 결제 건수의 합
	 * (int64)
	 */
	totalCount: number
}
