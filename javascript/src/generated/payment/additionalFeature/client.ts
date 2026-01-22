import { AdditionalFeatureError } from "./AdditionalFeatureError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ChannelNotFoundError } from "../../../generated/common/ChannelNotFoundError"
import type { GetPgCardPromotionsResponse } from "../../../generated/payment/additionalFeature/GetPgCardPromotionsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PgPromotionCardCompany } from "../../../generated/payment/additionalFeature/PgPromotionCardCompany"
import type { PgProviderError } from "../../../generated/common/PgProviderError"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function AdditionalFeatureClient(init: PortOneClientInit): AdditionalFeatureClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPgCardPromotions: async (
			options: {
				channelKey: string,
				amount: number,
				cardCompany?: PgPromotionCardCompany,
			}
		): Promise<GetPgCardPromotionsResponse> => {
			const {
				channelKey,
				amount,
				cardCompany,
			} = options
			const query = [
				["channelKey", channelKey],
				["amount", amount],
				["cardCompany", cardCompany],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payment-gateways/card-promotion?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPgCardPromotionsError(await response.json())
			}
			return response.json()
		},
	}
}
export type AdditionalFeatureClient = {
	/**
	 * PG사 카드 프로모션 조회 API
	 *
	 * 주어진 채널에 대해 PG사에서 제공하는 카드 프로모션 목록을 조회합니다.
	 * 해당 API는 현재 특정 PG사(KCP_V2)에 대해서만 지원되며, 지원 여부는 포트원 기술지원팀에 문의 부탁드립니다.
	 *
	 * @throws {@link GetPgCardPromotionsError}
	 */
	getPgCardPromotions: (
		options: {
			/**
			 * 채널 키
			 *
			 * 조회하고자 하는 채널의 키
			 */
			channelKey: string,
			/**
			 * 결제 금액
			 *
			 * 결제 금액입니다. 해당 결제 금액 기준 이용 가능한 프로모션 목록이 조회됩니다.
			 * (int64)
			 */
			amount: number,
			/**
			 * 카드사 필터
			 *
			 * 조회할 카드사입니다. 값을 입력하지 않으면 카드사 필터링이 적용되지 않습니다.
			 */
			cardCompany?: PgPromotionCardCompany,
		}
	) => Promise<GetPgCardPromotionsResponse>
}
export class GetPgCardPromotionsError extends AdditionalFeatureError {
	declare readonly data: ChannelNotFoundError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ChannelNotFoundError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPgCardPromotionsError.prototype)
		this.name = "GetPgCardPromotionsError"
	}
}
