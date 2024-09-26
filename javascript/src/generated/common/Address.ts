import type { OneLineAddress } from "#generated/common/OneLineAddress"
import type { SeparatedAddress } from "#generated/common/SeparatedAddress"

/**
 * 분리 형식 주소
 *
 * oneLine(한 줄 형식 주소) 필드는 항상 존재합니다.
 */
export type Address =
	/** 한 줄 형식 */
	| OneLineAddress
	/** 분리 형식 */
	| SeparatedAddress
