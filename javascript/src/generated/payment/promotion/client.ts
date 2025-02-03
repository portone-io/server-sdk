import { PromotionError } from "./PromotionError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { Promotion } from "../../../generated/payment/promotion/Promotion"
import type { PromotionNotFoundError } from "../../../generated/payment/promotion/PromotionNotFoundError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
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
				throw new GetPromotionError(await response.json())
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
export class GetPromotionError extends PromotionError {
	declare readonly data: ForbiddenError | InvalidRequestError | PromotionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PromotionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPromotionError.prototype)
		this.name = "GetPromotionError"
	}
}
