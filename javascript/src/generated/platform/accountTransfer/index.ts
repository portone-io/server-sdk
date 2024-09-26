export type * from "./GetAccountTransfersBody"
export type * from "./GetPlatformAccountTransfersError"
export type * from "./GetPlatformAccountTransfersResponse"
export type * from "./PlatformAccountTransfer"
export type * from "./PlatformAccountTransferFilter"
export type * from "./PlatformAccountTransferType"
export type * from "./PlatformDepositAccountTransfer"
export type * from "./PlatformPartnerPayoutAccountTransfer"
export type * from "./PlatformRemitAccountTransfer"
import type { GetPlatformAccountTransfersResponse } from "#generated/platform/accountTransfer/GetPlatformAccountTransfersResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformAccountTransferFilter } from "#generated/platform/accountTransfer/PlatformAccountTransferFilter"

export type Operations = {
	/**
	 * 이체 내역 다건 조회
	 *
	 * 여러 이체 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAccountTransfers: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformAccountTransferFilter,
		}
	) => Promise<GetPlatformAccountTransfersResponse>
}
