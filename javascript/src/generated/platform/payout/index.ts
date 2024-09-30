import type { GetPlatformPayoutsError } from "#generated/platform/payout/GetPlatformPayoutsError"
import type { GetPlatformPayoutsResponse } from "#generated/platform/payout/GetPlatformPayoutsResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformPayoutFilterInput } from "#generated/platform/payout/PlatformPayoutFilterInput"
import * as Errors from "#generated/errors"
export type { GetPlatformPayoutsBody } from "./GetPlatformPayoutsBody"
export type { GetPlatformPayoutsResponse } from "./GetPlatformPayoutsResponse"
export type { PlatformPayout } from "./PlatformPayout"
export type { PlatformPayoutAccount } from "./PlatformPayoutAccount"
export type { PlatformPayoutFilterInput } from "./PlatformPayoutFilterInput"
export type { PlatformPayoutFilterInputCriteria } from "./PlatformPayoutFilterInputCriteria"
export type { PlatformPayoutStatus } from "./PlatformPayoutStatus"
/** @ignore */
export function PayoutClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PayoutClient {
	return {
		getPlatformPayouts: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformPayoutFilterInput,
			}
		): Promise<GetPlatformPayoutsResponse> => {
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
				new URL(`/platform/payouts?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPayoutsError = await response.json()
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
export type PayoutClient = {
	/**
	 * 지급 내역 다건 조회
	 *
	 * 여러 지급 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformPayoutFilterInput,
		}
	) => Promise<GetPlatformPayoutsResponse>
}

