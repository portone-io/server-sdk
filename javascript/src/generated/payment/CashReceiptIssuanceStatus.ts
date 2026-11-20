/** 현금영수증 발행여부 */
export type CashReceiptIssuanceStatus =
	/** 발행 완료 */
	| "ISSUED"
	/** 미발행 */
	| "NOT_ISSUED"
	| string & {}
