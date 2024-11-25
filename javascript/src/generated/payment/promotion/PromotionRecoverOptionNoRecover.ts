import type { PromotionSpareBudget } from "./../../payment/promotion/PromotionSpareBudget"
/** 결제 취소 시 프로모션 예산 미복구 */
export type PromotionRecoverOptionNoRecover = {
	/** 결제 취소 시 프로모션 예산 복구 옵션 */
	type: "NO_RECOVER"
	spareBudget?: PromotionSpareBudget
}
