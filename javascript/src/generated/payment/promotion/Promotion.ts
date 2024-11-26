import type { Unrecognized } from "./../../../utils/unrecognized"
import type { CardPromotion } from "./../../payment/promotion/CardPromotion"
/** 프로모션 */
export type Promotion =
	/** 카드 프로모션 */
	| CardPromotion
	| { readonly type: Unrecognized }

export function isUnrecognizedPromotion(entity: Promotion): entity is { readonly type: Unrecognized } {
	return entity.type !== "CARD"
}
