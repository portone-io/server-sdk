import type { PromotionAmountDiscount } from "#generated/payment/promotion/PromotionAmountDiscount"
import type { PromotionPercentDiscount } from "#generated/payment/promotion/PromotionPercentDiscount"

export type PromotionDiscount =
	/** 정액 할인 */
	| PromotionAmountDiscount
	/** 정률 할인 */
	| PromotionPercentDiscount
