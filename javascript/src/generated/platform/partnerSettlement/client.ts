import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { GetPlatformPartnerSettlementsResponse } from "../../../generated/platform/partnerSettlement/GetPlatformPartnerSettlementsResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformPartnerSettlementFilterInput } from "../../../generated/platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
import type { GetPlatformPartnerSettlementsError as _InternalGetPlatformPartnerSettlementsError } from "../../../generated/platform/partnerSettlement/GetPlatformPartnerSettlementsError"
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
				const errorResponse: _InternalGetPlatformPartnerSettlementsError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
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
export type GetPlatformPartnerSettlementsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformPartnerSettlementsError(error: Error): error is GetPlatformPartnerSettlementsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
