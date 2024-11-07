import type { PlatformFeeInput } from "./../../platform/PlatformFeeInput"
import type { PlatformPayer } from "./../../platform/PlatformPayer"

/** 추가 수수료 정책 생성을 위한 입력 정보 */
export type CreatePlatformAdditionalFeePolicyBody = {
	/**
	 * 생성할 추가 수수료 정책 아이디
	 *
	 * 명시하지 않으면 id 가 임의로 생성됩니다.
	 */
	id?: string
	/** 이름 */
	name: string
	/** 수수료 정보 */
	fee: PlatformFeeInput
	/** 메모 */
	memo?: string
	/** 부가세 부담 주체 */
	vatPayer: PlatformPayer
}
