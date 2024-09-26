export type PlatformCancellableDiscountAmountExceededError = {
	type: "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED"
	discountSharePolicyId: string
	discountSharePolicyGraphqlId: string
	/** (int64) */
	cancellableAmount: number
	/** (int64) */
	requestAmount: number
	productId?: string
	message?: string
}
