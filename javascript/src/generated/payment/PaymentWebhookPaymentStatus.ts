/** 웹훅 발송 시 결제 건 상태 */
export type PaymentWebhookPaymentStatus =
	| "VIRTUAL_ACCOUNT_ISSUED"
	| "PAID"
	| "READY"
	| "FAILED"
	| "PAY_PENDING"
	| "CANCELLED"
	| "PARTIAL_CANCELLED"
