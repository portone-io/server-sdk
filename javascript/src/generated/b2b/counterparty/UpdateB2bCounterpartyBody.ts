import type { B2bCounterpartyCreateOptions } from "./../../b2b/counterparty/B2bCounterpartyCreateOptions"
import type { B2bCounterpartyInput } from "./../../b2b/counterparty/B2bCounterpartyInput"
/** 거래처 정보 수정 요청 */
export type UpdateB2bCounterpartyBody = {
	/** 거래처 정보 */
	counterparty: B2bCounterpartyInput
	/**
	 * 확인 옵션
	 *
	 * 사업자 정보 및 휴폐업 상태 조회 옵션입니다.
	 */
	options?: B2bCounterpartyCreateOptions
}
