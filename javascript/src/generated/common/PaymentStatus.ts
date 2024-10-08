/** 결제 건 상태 */
export type PaymentStatus =
	| "READY"
	| "PENDING"
	| "VIRTUAL_ACCOUNT_ISSUED"
	| "PAID"
	| "FAILED"
	| "PARTIAL_CANCELLED"
	| "CANCELLED"
