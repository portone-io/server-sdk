export type * from "./GetPlatformPayoutsBody"
export type * from "./GetPlatformPayoutsError"
export type * from "./GetPlatformPayoutsResponse"
export type * from "./PlatformPayout"
export type * from "./PlatformPayoutAccount"
export type * from "./PlatformPayoutFilterInput"
export type * from "./PlatformPayoutFilterInputCriteria"
export type * from "./PlatformPayoutStatus"
import type { GetPlatformPayoutsResponse } from "#generated/platform/payout/GetPlatformPayoutsResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformPayoutFilterInput } from "#generated/platform/payout/PlatformPayoutFilterInput"

export type Operations = {
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
