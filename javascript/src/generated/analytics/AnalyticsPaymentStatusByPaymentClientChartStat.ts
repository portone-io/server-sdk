import type { PaymentClientType } from "#generated/common/PaymentClientType"
import type { PaymentStatus } from "#generated/common/PaymentStatus"

/** 고객사의 결제 환경 별 결제 상태 차트 정보 */
export type AnalyticsPaymentStatusByPaymentClientChartStat = {
	/** 결제가 발생한 클라이언트 환경 */
	paymentClientType: PaymentClientType
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
