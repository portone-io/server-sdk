/** 빌링키가 존재하지 않는 경우 */
export type BillingKeyNotFoundError = {
	type: "BILLING_KEY_NOT_FOUND"
	message?: string
}
