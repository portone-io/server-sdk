import type { B2bCounterpartyContactInput } from "./../../b2b/counterparty/B2bCounterpartyContactInput"
/** 거래처 입력 정보 */
export type B2bCounterpartyInput = {
	/**
	 * 사업자등록번호
	 *
	 * `-` 없이 숫자로만 구성됩니다.
	 */
	brn: string
	/** 거래처명 */
	name?: string
	/** 대표자 성명 */
	representativeName?: string
	/** 주소 */
	address?: string
	/** 업태 */
	businessType?: string
	/** 업종 */
	businessClass?: string
	/** 담당자 정보 */
	contact?: B2bCounterpartyContactInput
	/**
	 * 추가 담당자 목록
	 *
	 * 최대 5명까지 등록할 수 있습니다.
	 */
	additionalContacts?: B2bCounterpartyContactInput[]
	/** 메모 */
	memo?: string
}
