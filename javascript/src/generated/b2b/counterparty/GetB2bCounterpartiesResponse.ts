import type { B2bCounterparty } from "./../../b2b/counterparty/B2bCounterparty"
import type { PageInfo } from "./../../common/PageInfo"
/** 거래처 검색 성공 응답 */
export type GetB2bCounterpartiesResponse = {
	/** 페이지 정보 */
	page: PageInfo
	/** 거래처 목록 */
	items: B2bCounterparty[]
}
