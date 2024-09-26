export type PlatformTransferDiscountSharePolicyNotFoundError = {
	type: "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND"
	discountSharePolicyId: string
	discountSharePolicyGraphqlId: string
	productId?: string
	message?: string
}
