import type { PaymentMethodType } from "#generated/common/PaymentMethodType"

/** 결제수단별 결제금액, 결제 건수를 나타냅니다. */
export type AnalyticsPaymentMethodChartStat = {
	/** 결제수단 */
	paymentMethod?: PaymentMethodType
	/**
	 * 결제수단별 결제금액
	 * (int64)
	 */
	amount: number
	/**
	 * 결제수단별 결제 건수
	 * (int64)
	 */
	count: number
}
