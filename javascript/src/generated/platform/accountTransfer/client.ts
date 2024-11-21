import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { GetPlatformAccountTransfersResponse } from "../../../generated/platform/accountTransfer/GetPlatformAccountTransfersResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAccountTransferFilter } from "../../../generated/platform/accountTransfer/PlatformAccountTransferFilter"
import type { GetPlatformAccountTransfersError as _InternalGetPlatformAccountTransfersError } from "../../../generated/platform/accountTransfer/GetPlatformAccountTransfersError"
export function AccountTransferClient(init: PortOneClientInit): AccountTransferClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformAccountTransfers: async (
			options?: {
				isForTest?: boolean,
				page?: PageInput,
				filter?: PlatformAccountTransferFilter,
			}
		): Promise<GetPlatformAccountTransfersResponse> => {
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
				new URL(`/platform/account-transfers?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformAccountTransfersError = await response.json()
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
export type AccountTransferClient = {
	/**
	 * 이체 내역 다건 조회
	 *
	 * 여러 이체 내역을 조회합니다.
	 *
	 * @throws {@link GetPlatformAccountTransfersError}
	 */
	getPlatformAccountTransfers: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformAccountTransferFilter,
		}
	) => Promise<GetPlatformAccountTransfersResponse>
}
export type GetPlatformAccountTransfersError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformAccountTransfersError(error: Error): error is GetPlatformAccountTransfersError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
