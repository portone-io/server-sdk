import type { PromotionAmountDiscountScheme } from "./../../payment/promotion/PromotionAmountDiscountScheme"
import type { PromotionPercentDiscountScheme } from "./../../payment/promotion/PromotionPercentDiscountScheme"

export type PromotionDiscountScheme =
	/** 정액 할인 */
	| PromotionAmountDiscountScheme
	/** 정률 할인 */
	| PromotionPercentDiscountScheme
	| { readonly type: unique symbol }
