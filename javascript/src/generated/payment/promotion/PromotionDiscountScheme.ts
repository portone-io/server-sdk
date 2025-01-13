import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PromotionAmountDiscountScheme } from "./../../payment/promotion/PromotionAmountDiscountScheme"
import type { PromotionPercentDiscountScheme } from "./../../payment/promotion/PromotionPercentDiscountScheme"
export type PromotionDiscountScheme =
	/** 정액 할인 */
	| PromotionAmountDiscountScheme
	/** 정률 할인 */
	| PromotionPercentDiscountScheme
	| { readonly type: Unrecognized }

export function isUnrecognizedPromotionDiscountScheme(entity: PromotionDiscountScheme): entity is { readonly type: Unrecognized } {
	return entity.type !== "AMOUNT"
		&& entity.type !== "PERCENT"
}
