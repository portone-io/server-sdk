/** 프로모션 할인 금액이 결제 시도 금액 이상인 경우 */
export type DiscountAmountExceedsTotalAmountError = {
	type: "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT"
	message?: string
}
