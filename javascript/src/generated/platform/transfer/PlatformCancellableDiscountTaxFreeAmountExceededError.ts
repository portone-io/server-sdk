export type PlatformCancellableDiscountTaxFreeAmountExceededError = {
	type: "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED"
	discountSharePolicyId: string
	discountSharePolicyGraphqlId: string
	/** (int64) */
	cancellableAmount: number
	/** (int64) */
	requestAmount: number
	productId?: string
	message?: string
}
