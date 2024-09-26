/** 거래대사 매치 실패 사유 */
export type PaymentReconciliationNotMatchedReason =
	/** 에스크로 여부 불일치 */
	| "ESCROW_NOT_MATCHED"
	/** 할부 개월 수 불일치 */
	| "INSTALLMENT_MONTH_NOT_MATCHED"
	/** 면세 금액 불일치 */
	| "TAX_FREE_AMOUNT_NOT_MATCHED"
	/** 결제 금액 불일치 */
	| "PAYMENT_AMOUNT_NOT_MATCHED"
	/** 결제일자 불일치 */
	| "PAYMENT_DATE_NOT_MATCHED"
	/** 부가세 금액 불일치 */
	| "VAT_AMOUNT_NOT_MATCHED"
