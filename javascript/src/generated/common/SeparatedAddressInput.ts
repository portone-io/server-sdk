import type { Country } from "#generated/common/Country"

/** 분리 형식 주소 입력 정보 */
export type SeparatedAddressInput = {
	/** 상세 주소 1 */
	addressLine1: string
	/** 상세 주소 2 */
	addressLine2: string
	/** 시/군/구 */
	city?: string
	/** 주/도/시 */
	province?: string
	/** 국가 */
	country?: Country
}
