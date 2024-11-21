import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { GetPlatformPayoutsResponse } from "../../../generated/platform/payout/GetPlatformPayoutsResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformPayoutFilterInput } from "../../../generated/platform/payout/PlatformPayoutFilterInput"
import type { GetPlatformPayoutsError as _InternalGetPlatformPayoutsError } from "../../../generated/platform/payout/GetPlatformPayoutsError"
export function PayoutClient(init: PortOneClientInit): PayoutClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformPayoutsError = await response.json()
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
	 * @throws {@link GetPlatformPayoutsError}
	 */
	getPlatformPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformPayoutFilterInput,
		}
	) => Promise<GetPlatformPayoutsResponse>
}
export type GetPlatformPayoutsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformPayoutsError(error: Error): error is GetPlatformPayoutsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
