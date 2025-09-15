/** 과세 유형 */
export type B2bTaxInvoiceTaxationType =
	/** 과세 */
	| "TAXABLE"
	/** 영세 */
	| "ZERO_RATED"
	/** 면세 */
	| "FREE"
	| string & {}
