/** 영수/청구 */
export type B2bTaxInvoicePurposeType =
	/** 영수 */
	| "RECEIPT"
	/** 청구 */
	| "INVOICE"
	/** 없음 */
	| "NONE"
	| string & {}
