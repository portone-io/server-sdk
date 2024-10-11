import type { GetPlatformAccountTransfersError } from "#generated/platform/accountTransfer/GetPlatformAccountTransfersError"
import type { GetPlatformAccountTransfersResponse } from "#generated/platform/accountTransfer/GetPlatformAccountTransfersResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformAccountTransferFilter } from "#generated/platform/accountTransfer/PlatformAccountTransferFilter"
import * as Errors from "#generated/errors"
export type { GetAccountTransfersBody } from "./GetAccountTransfersBody"
export type { GetPlatformAccountTransfersResponse } from "./GetPlatformAccountTransfersResponse"
export type { PlatformAccountTransfer } from "./PlatformAccountTransfer"
export type { PlatformAccountTransferFilter } from "./PlatformAccountTransferFilter"
export type { PlatformAccountTransferType } from "./PlatformAccountTransferType"
export type { PlatformDepositAccountTransfer } from "./PlatformDepositAccountTransfer"
export type { PlatformPartnerPayoutAccountTransfer } from "./PlatformPartnerPayoutAccountTransfer"
export type { PlatformRemitAccountTransfer } from "./PlatformRemitAccountTransfer"
/** @ignore */
export function AccountTransferClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): AccountTransferClient {
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
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformAccountTransfersError = await response.json()
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPlatformAccountTransfers: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformAccountTransferFilter,
		}
	) => Promise<GetPlatformAccountTransfersResponse>
}

