import type { GetPlatformBulkPayoutsError } from "../..//platform/bulkPayout/GetPlatformBulkPayoutsError"
import type { GetPlatformBulkPayoutsResponse } from "../..//platform/bulkPayout/GetPlatformBulkPayoutsResponse"
import type { PageInput } from "../..//common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "../..//platform/bulkPayout/PlatformBulkPayoutFilterInput"
import * as Errors from "../..//errors"
export type { GetPlatformBulkPayoutsBody } from "./GetPlatformBulkPayoutsBody"
export type { GetPlatformBulkPayoutsResponse } from "./GetPlatformBulkPayoutsResponse"
export type { PlatformBulkPayout } from "./PlatformBulkPayout"
export type { PlatformBulkPayoutFilterInput } from "./PlatformBulkPayoutFilterInput"
export type { PlatformBulkPayoutFilterInputCriteria } from "./PlatformBulkPayoutFilterInputCriteria"
export type { PlatformBulkPayoutStats } from "./PlatformBulkPayoutStats"
export type { PlatformBulkPayoutStatus } from "./PlatformBulkPayoutStatus"
export type { PlatformBulkPayoutStatusStats } from "./PlatformBulkPayoutStatusStats"
/** @ignore */
export function BulkPayoutClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): BulkPayoutClient {
	return {
		getPlatformBulkPayouts: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformBulkPayoutFilterInput,
			}
		): Promise<GetPlatformBulkPayoutsResponse> => {
			const isForTest = options?.isForTest
			const page = options?.page
			const filter = options?.filter
			const requestBody = JSON.stringify({
				isForTest,
				page,
				filter,
			})
			const query = [
				["requestBody", requestBody],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/bulk-payouts?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformBulkPayoutsError = await response.json()
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
export type BulkPayoutClient = {
	/**
	 * 일괄 지급 내역 다건 조회
	 *
	 * 성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPlatformBulkPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformBulkPayoutFilterInput,
		}
	) => Promise<GetPlatformBulkPayoutsResponse>
}

