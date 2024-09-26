export type * from "./CardPromotion"
export type * from "./GetPromotionError"
export type * from "./Promotion"
export type * from "./PromotionAmountDiscount"
export type * from "./PromotionCardCompany"
export type * from "./PromotionDiscount"
export type * from "./PromotionNotFoundError"
export type * from "./PromotionPercentDiscount"
export type * from "./PromotionStatus"
import type { Promotion } from "#generated/promotion/Promotion"

export type Operations = {
	/**
	 * 프로모션 단건 조회
	 *
	 * 주어진 아이디에 대응되는 프로모션을 조회합니다.
	 *
	 * @param promotionId
	 * 조회할 프로모션 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PromotionNotFoundError} 프로모션이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPromotion: (
		/** 조회할 프로모션 아이디 */
		promotionId: string,
	) => Promise<Promotion>
}
