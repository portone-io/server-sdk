/** 결제 건 상태 */
export type PaymentStatus =
	| "PENDING"
	| "VIRTUAL_ACCOUNT_ISSUED"
	| "PAID"
	| "READY"
	| "FAILED"
	| "CANCELLED"
	| "PARTIAL_CANCELLED"
