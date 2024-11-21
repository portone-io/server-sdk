import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { GetPlatformBulkPayoutsResponse } from "../../../generated/platform/bulkPayout/GetPlatformBulkPayoutsResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "../../../generated/platform/bulkPayout/PlatformBulkPayoutFilterInput"
import type { GetPlatformBulkPayoutsError as _InternalGetPlatformBulkPayoutsError } from "../../../generated/platform/bulkPayout/GetPlatformBulkPayoutsError"
export function BulkPayoutClient(init: PortOneClientInit): BulkPayoutClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
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
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformBulkPayoutsError = await response.json()
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
	 * @throws {@link GetPlatformBulkPayoutsError}
	 */
	getPlatformBulkPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformBulkPayoutFilterInput,
		}
	) => Promise<GetPlatformBulkPayoutsResponse>
}
export type GetPlatformBulkPayoutsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformBulkPayoutsError(error: Error): error is GetPlatformBulkPayoutsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
