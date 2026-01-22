import type { PgPromotionCardCompany } from "./../../payment/additionalFeature/PgPromotionCardCompany"
/**
 * PG사 카드 프로모션
 *
 * PG사에서 제공하는 카드 프로모션 정보입니다.
 */
export type PgCardPromotion = {
	/**
	 * 프로모션 아이디
	 *
	 * PG사에서 부여한 프로모션 식별자입니다.
	 */
	promotionId: string
	/**
	 * 카드사
	 *
	 * 프로모션이 적용되는 카드사입니다.
	 */
	cardCompany: PgPromotionCardCompany
	/**
	 * 할인 금액
	 *
	 * 프로모션 적용 시 할인되는 금액입니다.
	 * (int64)
	 */
	discountAmount: number
	/**
	 * 최소 결제 금액
	 *
	 * 프로모션이 적용되기 위한 최소 결제 금액입니다.
	 * (int64)
	 */
	minimumPaymentAmount: number
}
