/** 프로모션이 존재하지 않는 경우 */
export type PromotionNotFoundError = {
	type: "PROMOTION_NOT_FOUND"
	message?: string
}
