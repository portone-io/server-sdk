import type { PaymentStatus } from "#generated/common/PaymentStatus"
import type { PgCompany } from "#generated/common/PgCompany"

/** 각 상태의 건수와 금액, 사분위수를 나타냅니다. */
export type AnalyticsPaymentStatusByPgCompanyChartStat = {
	/** PG사 */
	pgCompany: PgCompany
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
