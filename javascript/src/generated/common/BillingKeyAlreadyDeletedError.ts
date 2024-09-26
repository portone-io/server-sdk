/** 빌링키가 이미 삭제된 경우 */
export type BillingKeyAlreadyDeletedError = {
	type: "BILLING_KEY_ALREADY_DELETED"
	message?: string
}
