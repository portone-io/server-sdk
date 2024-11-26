import type { CustomerSeparatedName } from "./../common/CustomerSeparatedName"
/**
 * 고객 이름 입력 정보
 *
 * 두 개의 이름 형식 중 한 가지만 선택하여 입력해주세요.
 */
export type CustomerNameInput = {
	/** 한 줄 이름 형식 */
	full?: string
	/** 분리형 이름 형식 */
	separated?: CustomerSeparatedName
}
