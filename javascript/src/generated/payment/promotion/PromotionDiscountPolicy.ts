import type { PromotionDiscountPartition } from "./../../payment/promotion/PromotionDiscountPartition"

/** 프로모션 할인 정책 */
export type PromotionDiscountPolicy = {
	/** 금액 구간별 프로모션 할인 정책 */
	partitions: PromotionDiscountPartition[]
}
