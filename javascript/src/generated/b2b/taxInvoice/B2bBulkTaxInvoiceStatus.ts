/** 일괄 세금계산서 상태 */
export type B2bBulkTaxInvoiceStatus =
	| "DRAFT_PENDING"
	| "DRAFTED"
	| "REQUEST_PENDING"
	| "ISSUE_PENDING"
	| "IN_PROGRESS"
	| "COMPLETED"
	| "FAILED"
	| "CANCELLED"
	| string & {}
