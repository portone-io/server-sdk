import type { PromotionSpareBudgetAmount } from "./../../payment/promotion/PromotionSpareBudgetAmount"
import type { PromotionSpareBudgetPercent } from "./../../payment/promotion/PromotionSpareBudgetPercent"

export type PromotionSpareBudget =
	/** 추가 예산 금액 */
	| PromotionSpareBudgetAmount
	/** 추가 예산 비율 */
	| PromotionSpareBudgetPercent
	| { readonly type: unique symbol }
