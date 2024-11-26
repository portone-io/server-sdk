import { PartnerSettlementError } from "./PartnerSettlementError"
import type { Unrecognized } from "./../../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformPartnerSettlementsResponse } from "../../../generated/platform/partnerSettlement/GetPlatformPartnerSettlementsResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerSettlementFilterInput } from "../../../generated/platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
export function PartnerSettlementClient(init: PortOneClientInit): PartnerSettlementClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformPartnerSettlements: async (
			options: {
				page?: PageInput,
				filter: PlatformPartnerSettlementFilterInput,
				isForTest: boolean,
			}
		): Promise<GetPlatformPartnerSettlementsResponse> => {
			const {
				page,
				filter,
				isForTest,
			} = options
			const requestBody = JSON.stringify({
				page,
				filter,
				isForTest,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-settlements?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformPartnerSettlementsError(await response.json())
			}
			return response.json()
		},
	}
}
export type PartnerSettlementClient = {
	/**
	 * 정산 내역 다건 조회
	 *
	 * 여러 정산 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerSettlementsError}
	 */
	getPlatformPartnerSettlements: (
		options: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 정산내역 조건 필터 */
			filter: PlatformPartnerSettlementFilterInput,
			isForTest: boolean,
		}
	) => Promise<GetPlatformPartnerSettlementsResponse>
}
export class GetPlatformPartnerSettlementsError extends PartnerSettlementError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerSettlementsError.prototype)
		this.name = "GetPlatformPartnerSettlementsError"
	}
}
