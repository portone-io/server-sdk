import type { PaymentStatus } from "#generated/common/PaymentStatus"

/** 각 상태의 건수와 금액, 사분위수를 나타냅니다. */
export type AnalyticsPaymentStatusChartStat = {
	/** 결제 건 상태 */
	paymentStatus: PaymentStatus
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
	/**
	 * 해당 상태 비율
	 * (int64)
	 */
	averageRatio: number
	/**
	 * 1 사분위수
	 * (int64)
	 */
	firstQuantile: number
	/**
	 * 중앙값
	 * (int64)
	 */
	median: number
	/**
	 * 3 사분위수
	 * (int64)
	 */
	thirdQuantile: number
}
