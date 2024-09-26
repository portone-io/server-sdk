export type * from "./GetPlatformBulkPayoutsBody"
export type * from "./GetPlatformBulkPayoutsError"
export type * from "./GetPlatformBulkPayoutsResponse"
export type * from "./PlatformBulkPayout"
export type * from "./PlatformBulkPayoutFilterInput"
export type * from "./PlatformBulkPayoutFilterInputCriteria"
export type * from "./PlatformBulkPayoutStats"
export type * from "./PlatformBulkPayoutStatus"
export type * from "./PlatformBulkPayoutStatusStats"
import type { GetPlatformBulkPayoutsResponse } from "#generated/platform/bulkPayout/GetPlatformBulkPayoutsResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "#generated/platform/bulkPayout/PlatformBulkPayoutFilterInput"

export type Operations = {
	/**
	 * 일괄 지급 내역 다건 조회
	 *
	 * 성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformBulkPayouts: (
		options?: {
			isForTest?: boolean,
			page?: PageInput,
			filter?: PlatformBulkPayoutFilterInput,
		}
	) => Promise<GetPlatformBulkPayoutsResponse>
}
