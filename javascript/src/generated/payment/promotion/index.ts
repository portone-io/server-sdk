import type { GetPromotionError } from "../..//payment/promotion/GetPromotionError"
import type { Promotion } from "../..//payment/promotion/Promotion"
import * as Errors from "../..//errors"
export type { CardPromotion } from "./CardPromotion"
export type { Promotion } from "./Promotion"
export type { PromotionAmountDiscount } from "./PromotionAmountDiscount"
export type { PromotionCardCompany } from "./PromotionCardCompany"
export type { PromotionDiscount } from "./PromotionDiscount"
export type { PromotionPercentDiscount } from "./PromotionPercentDiscount"
export type { PromotionStatus } from "./PromotionStatus"
/** @ignore */
export function PromotionClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PromotionClient {
	return {
		getPromotion: async (
			promotionId: string,
		): Promise<Promotion> => {
			const response = await fetch(
				new URL(`/promotions/${encodeURIComponent(promotionId)}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPromotionError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PROMOTION_NOT_FOUND":
					throw new Errors.PromotionNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
	}
}
export type PromotionClient = {
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
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPromotion: (
		/** 조회할 프로모션 아이디 */
		promotionId: string,
	) => Promise<Promotion>
}

