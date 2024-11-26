/** 웹훅 전송 상태 */
export type PaymentWebhookStatus =
	| "SUCCEEDED"
	| "FAILED_NOT_OK_RESPONSE"
	| "FAILED_UNEXPECTED_ERROR"
	| string & {}
