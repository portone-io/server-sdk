/** 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우 */
export type MaxWebhookRetryCountReachedError = {
	type: "MAX_WEBHOOK_RETRY_COUNT_REACHED"
	message?: string
}
