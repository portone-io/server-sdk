import type { PgCardPromotion } from "./../../payment/additionalFeature/PgCardPromotion"
/** PG사 카드 프로모션 조회 응답 */
export type GetPgCardPromotionsResponse = {
	/** 카드 프로모션 목록 */
	promotions?: PgCardPromotion[]
}
