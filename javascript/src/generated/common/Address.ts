import type { Unrecognized } from "./../../utils/unrecognized"
import type { OneLineAddress } from "./../common/OneLineAddress"
import type { SeparatedAddress } from "./../common/SeparatedAddress"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedAddress(entity: Address): entity is { readonly type: Unrecognized } {
	return entity.type !== "ONE_LINE"
		&& entity.type !== "SEPARATED"
}
