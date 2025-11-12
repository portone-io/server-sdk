import type { PageInput } from "./../../common/PageInput"
import type { PlatformPartnerSettlementFilterInput } from "./../../platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
/** 정산내역 다건 조회를 위한 입력 정보 */
export type GetPlatformPartnerSettlementsBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 정산내역 조건 필터 */
	filter: PlatformPartnerSettlementFilterInput
	/**
	 * 테스트 모드 여부
	 *
	 * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
	 * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
	 */
	isForTest?: boolean
}
