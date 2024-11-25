import type { Country } from "./../common/Country"
/**
 * 분리 형식 주소
 *
 * 한 줄 형식 주소와 분리 형식 주소 모두 존재합니다.
 * 한 줄 형식 주소는 분리 형식 주소를 이어 붙인 형태로 생성됩니다.
 */
export type SeparatedAddress = {
	type: "SEPARATED"
	/** 주소 (한 줄) */
	oneLine: string
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
