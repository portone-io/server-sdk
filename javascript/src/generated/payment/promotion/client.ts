import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { Promotion } from "../../../generated/payment/promotion/Promotion"
import type { GetPromotionError as _InternalGetPromotionError } from "../../../generated/payment/promotion/GetPromotionError"
export function PromotionClient(init: PortOneClientInit): PromotionClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPromotion: async (
			options: {
				promotionId: string,
			}
		): Promise<Promotion> => {
			const {
				promotionId,
			} = options
			const response = await fetch(
				new URL(`/promotions/${encodeURIComponent(promotionId)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPromotionError = await response.json()
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
	 * @throws {@link GetPromotionError}
	 */
	getPromotion: (
		options: {
			/** 조회할 프로모션 아이디 */
			promotionId: string,
		}
	) => Promise<Promotion>
}
export type GetPromotionError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PromotionNotFoundError
	| Errors.UnauthorizedError
export function isGetPromotionError(error: Error): error is GetPromotionError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PromotionNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
