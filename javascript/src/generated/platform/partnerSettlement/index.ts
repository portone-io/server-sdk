import type { GetPlatformPartnerSettlementsError } from "../..//platform/partnerSettlement/GetPlatformPartnerSettlementsError"
import type { GetPlatformPartnerSettlementsResponse } from "../..//platform/partnerSettlement/GetPlatformPartnerSettlementsResponse"
import type { PageInput } from "../..//common/PageInput"
import type { PlatformPartnerSettlementFilterInput } from "../..//platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
import * as Errors from "../..//errors"
export type { GetPlatformPartnerSettlementsBody } from "./GetPlatformPartnerSettlementsBody"
export type { GetPlatformPartnerSettlementsResponse } from "./GetPlatformPartnerSettlementsResponse"
export type { PlatformPartnerManualSettlement } from "./PlatformPartnerManualSettlement"
export type { PlatformPartnerOrderCancelSettlement } from "./PlatformPartnerOrderCancelSettlement"
export type { PlatformPartnerOrderSettlement } from "./PlatformPartnerOrderSettlement"
export type { PlatformPartnerSettlement } from "./PlatformPartnerSettlement"
export type { PlatformPartnerSettlementFilterInput } from "./PlatformPartnerSettlementFilterInput"
export type { PlatformPartnerSettlementFilterKeywordInput } from "./PlatformPartnerSettlementFilterKeywordInput"
export type { PlatformPartnerSettlementStatus } from "./PlatformPartnerSettlementStatus"
export type { PlatformPartnerSettlementStatusStats } from "./PlatformPartnerSettlementStatusStats"
export type { PlatformPartnerSettlementType } from "./PlatformPartnerSettlementType"
/** @ignore */
export function PartnerSettlementClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PartnerSettlementClient {
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPartnerSettlementsError = await response.json()
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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

