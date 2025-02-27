/** 현금영수증 발급 건 상태 */
export type CashReceiptStatus =
	| "ISSUED"
	| "CANCELLED"
	| "FAILED"
	| string & {}
