import type { PaymentMethodType } from "#generated/common/PaymentMethodType"

/** 특정 시점의 결제수단별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsPaymentMethodTrendChartStat = {
	/**
	 * 시점
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 결제수단 */
	paymentMethod?: PaymentMethodType
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
