import type { PaymentMethodType } from "#generated/common/PaymentMethodType"
import type { PaymentStatus } from "#generated/common/PaymentStatus"

/** 각 결제수단, 상태 별 건수와 금액을 나타냅니다. */
export type AnalyticsPaymentStatusByPaymentMethodChartStat = {
	/** 결제수단 */
	paymentMethod?: PaymentMethodType
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
}
