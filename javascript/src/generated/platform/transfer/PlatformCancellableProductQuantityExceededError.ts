export type PlatformCancellableProductQuantityExceededError = {
	type: "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED"
	productId: string
	/** (int64) */
	cancellableQuantity: number
	message?: string
}
