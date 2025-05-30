import type { PageInput } from "./../../common/PageInput"
import type { PlatformTransferFilterInput } from "./../../platform/transfer/PlatformTransferFilterInput"
/** 정산건 요약 다건 조회를 위한 입력 정보 */
export type GetPlatformTransferSummariesBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 정산건 조건 필터 */
	filter?: PlatformTransferFilterInput
}
