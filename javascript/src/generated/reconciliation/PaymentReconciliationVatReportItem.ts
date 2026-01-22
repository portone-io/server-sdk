import type { SimplifiedPaymentMethodType } from "./../reconciliation/SimplifiedPaymentMethodType"
export type PaymentReconciliationVatReportItem = {
	/** 결제수단 */
	paymentMethod: SimplifiedPaymentMethodType
	/**
	 * 공급가액
	 * (int64)
	 */
	supplyAmount: number
	/**
	 * 부가세 금액
	 * (int64)
	 */
	vatAmount: number
	/**
	 * 면세 금액
	 * (int64)
	 */
	taxFreeAmount: number
	/**
	 * 총 금액
	 * (int64)
	 */
	totalAmount: number
}
