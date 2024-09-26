export type PaymentReconciliationSettlementSummaryAggregate = {
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlementAmount: number
	/**
	 * 정산 건 수
	 * (int64)
	 */
	settlementCount: number
	/**
	 * PG 수수료
	 * (int64)
	 */
	feeAmount: number
	/**
	 * PG 수수료 부가세
	 * (int64)
	 */
	feeVatAmount: number
	/**
	 * 취소 금액
	 * (int64)
	 */
	cancelAmount: number
	/**
	 * 취소 건 수
	 * (int64)
	 */
	cancelCount: number
	/**
	 * 거래 합계 금액
	 * (int64)
	 */
	transactionAmount: number
}
