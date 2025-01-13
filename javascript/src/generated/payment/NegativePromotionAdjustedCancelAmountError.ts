/** 프로모션에 의해 조정된 취소 금액이 음수인 경우 */
export type NegativePromotionAdjustedCancelAmountError = {
	type: "NEGATIVE_PROMOTION_ADJUSTED_CANCEL_AMOUNT"
	message?: string
}
