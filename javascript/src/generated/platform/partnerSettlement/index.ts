export type * from "./GetPlatformPartnerSettlementsBody"
export type * from "./GetPlatformPartnerSettlementsError"
export type * from "./GetPlatformPartnerSettlementsResponse"
export type * from "./PlatformPartnerManualSettlement"
export type * from "./PlatformPartnerOrderCancelSettlement"
export type * from "./PlatformPartnerOrderSettlement"
export type * from "./PlatformPartnerSettlement"
export type * from "./PlatformPartnerSettlementFilterInput"
export type * from "./PlatformPartnerSettlementFilterKeywordInput"
export type * from "./PlatformPartnerSettlementStatus"
export type * from "./PlatformPartnerSettlementStatusStats"
export type * from "./PlatformPartnerSettlementType"
import type { GetPlatformPartnerSettlementsResponse } from "#generated/platform/partnerSettlement/GetPlatformPartnerSettlementsResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformPartnerSettlementFilterInput } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementFilterInput"

export type Operations = {
	/**
	 * 정산 내역 다건 조회
	 *
	 * 여러 정산 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartnerSettlements: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 정산내역 조건 필터 */
			filter?: PlatformPartnerSettlementFilterInput,
			isForTest?: boolean,
		}
	) => Promise<GetPlatformPartnerSettlementsResponse>
}
