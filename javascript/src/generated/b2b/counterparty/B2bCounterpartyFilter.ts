import type { B2bCounterpartyBusinessStatus } from "./../../b2b/counterparty/B2bCounterpartyBusinessStatus"
import type { B2bNtsConnectionStatus } from "./../../b2b/counterparty/B2bNtsConnectionStatus"
/** 거래처 검색 필터 */
export type B2bCounterpartyFilter = {
	/**
	 * 거래처 ID
	 *
	 * prefix 검색
	 */
	id?: string
	/** 사업자등록번호 */
	brn?: string
	/**
	 * 거래처명
	 *
	 * 포함 검색
	 */
	companyName?: string
	/** 대표자명 */
	representativeName?: string
	/** 담당자 이름 */
	contactName?: string
	/** 담당자 전화번호 */
	contactPhone?: string
	/** 담당자 이메일 */
	contactEmail?: string
	/** 휴폐업 상태 */
	businessStatuses?: B2bCounterpartyBusinessStatus[]
	/** 국세청 연동 상태 */
	ntsConnectionStatuses?: B2bNtsConnectionStatus[]
	/**
	 * 거래처 ID 목록
	 *
	 * 특정 ID 목록으로 필터링
	 */
	counterpartyIds?: string[]
}
