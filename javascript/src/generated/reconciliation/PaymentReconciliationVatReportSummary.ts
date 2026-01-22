export type PaymentReconciliationVatReportSummary = {
	/**
	 * 총 공급가액
	 * (int64)
	 */
	totalSupplyAmount: number
	/**
	 * 총 부가세 금액
	 * (int64)
	 */
	totalVatAmount: number
	/**
	 * 총 면세 금액
	 * (int64)
	 */
	totalTaxFreeAmount: number
	/**
	 * 총 금액
	 * (int64)
	 */
	totalAmount: number
}
