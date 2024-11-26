import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PromotionAmountDiscount } from "./../../payment/promotion/PromotionAmountDiscount"
import type { PromotionPercentDiscount } from "./../../payment/promotion/PromotionPercentDiscount"
export type PromotionDiscount =
	/** 정액 할인 */
	| PromotionAmountDiscount
	/** 정률 할인 */
	| PromotionPercentDiscount
	| { readonly type: Unrecognized }

export function isUnrecognizedPromotionDiscount(entity: PromotionDiscount): entity is { readonly type: Unrecognized } {
	return entity.type !== "AMOUNT"
		&& entity.type !== "PERCENT"
}
