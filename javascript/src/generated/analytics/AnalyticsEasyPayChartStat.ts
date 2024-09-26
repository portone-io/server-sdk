/** 특정 시점의 간편결제 거래 건수와 금액을 나타냅니다. */
export type AnalyticsEasyPayChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/**
	 * 거래액
	 * (int64)
	 */
	amount: number
	/**
	 * 거래 건수
	 * (int64)
	 */
	count: number
}
