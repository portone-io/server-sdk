import type { PromotionRecoverOptionNoRecover } from "./../../payment/promotion/PromotionRecoverOptionNoRecover"
import type { PromotionRecoverOptionRecover } from "./../../payment/promotion/PromotionRecoverOptionRecover"

export type PromotionRecoverOption =
	/** 결제 취소 시 프로모션 예산 미복구 */
	| PromotionRecoverOptionNoRecover
	/** 결제 취소 시 프로모션 예산 복구 */
	| PromotionRecoverOptionRecover
	| { readonly type: unique symbol }