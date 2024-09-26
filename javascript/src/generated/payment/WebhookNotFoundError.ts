/** 웹훅 내역이 존재하지 않는 경우 */
export type WebhookNotFoundError = {
	type: "WEBHOOK_NOT_FOUND"
	message?: string
}
