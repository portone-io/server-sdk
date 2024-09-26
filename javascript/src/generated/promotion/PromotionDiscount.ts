import type { PromotionAmountDiscount } from "#generated/promotion/PromotionAmountDiscount"
import type { PromotionPercentDiscount } from "#generated/promotion/PromotionPercentDiscount"

export type PromotionDiscount =
	/** 정액 할인 */
	| PromotionAmountDiscount
	/** 정률 할인 */
	| PromotionPercentDiscount
