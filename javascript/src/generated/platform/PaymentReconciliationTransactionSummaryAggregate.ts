export type PaymentReconciliationTransactionSummaryAggregate = {
	/**
	 * 거래 금액
	 * (int64)
	 */
	transactionAmount: number
	/**
	 * 거래 건 수
	 * (int64)
	 */
	transactionCount: number
	/**
	 * 거래 취소 금액
	 * (int64)
	 */
	cancelAmount: number
	/**
	 * 거래 취소 건 수
	 * (int64)
	 */
	cancelCount: number
	/**
	 * 거래 이상 금액
	 * (int64)
	 */
	anomalyAmount: number
	/**
	 * 거래 이상 건 수
	 * (int64)
	 */
	anomalyCount: number
	/**
	 * 대사불일치 건 수
	 * (int64)
	 */
	notMatchedCount: number
	/**
	 * 대사불능 건 수
	 * (int64)
	 */
	incomparableCount: number
}
