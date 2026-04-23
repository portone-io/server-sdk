import type { B2bCounterpartyFilter } from "./../../b2b/counterparty/B2bCounterpartyFilter"
import type { PageInput } from "./../../common/PageInput"
/** 거래처 검색 요청 정보 */
export type GetB2bCounterpartiesBody = {
	/** 페이지 정보 */
	page?: PageInput
	/** 검색 필터 */
	filter?: B2bCounterpartyFilter
}
