/** 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우 */
export type PromotionPayMethodDoesNotMatchError = {
	type: "PROMOTION_PAY_METHOD_DOES_NOT_MATCH"
	message?: string
}
