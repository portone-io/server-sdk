import type { PaymentWebhook } from "./../payment/PaymentWebhook"
/** 웹훅 재발송 응답 정보 */
export type ResendWebhookResponse = {
	/** 재발송 웹훅 정보 */
	webhook: PaymentWebhook
}
