/** 웹훅 발송 시 결제 건 상태 */
export type PaymentWebhookPaymentStatus =
	| "READY"
	| "VIRTUAL_ACCOUNT_ISSUED"
	| "PAID"
	| "FAILED"
	| "PARTIAL_CANCELLED"
	| "CANCELLED"
	| "PAY_PENDING"
	| string & {}
