import type { PromotionDiscountScheme } from "./../../payment/promotion/PromotionDiscountScheme"

/** 금액 구간별 프로모션 할인 정책 */
export type PromotionDiscountPartition = {
	/** (int64) */
	amountFrom: number
	scheme: PromotionDiscountScheme
}
