import type { B2bCounterpartyCreateOptions } from "./../../b2b/counterparty/B2bCounterpartyCreateOptions"
import type { B2bCounterpartyInput } from "./../../b2b/counterparty/B2bCounterpartyInput"
/** 거래처 생성 요청 정보 */
export type CreateB2bCounterpartyBody = {
	/**
	 * 거래처 아이디
	 *
	 * 입력하지 않으면 임의의 ID가 채번됩니다.
	 */
	counterpartyId?: string
	/** 거래처 정보 */
	counterparty: B2bCounterpartyInput
	/** 거래처 생성 옵션 */
	options?: B2bCounterpartyCreateOptions
}
