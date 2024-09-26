import type { PlatformFeeInput } from "#generated/platform/PlatformFeeInput"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"

/**
 * 추가 수수료 정책 업데이트를 위한 입력 정보
 *
 * 값이 명시하지 않은 필드는 업데이트되지 않습니다.
 */
export type UpdatePlatformAdditionalFeePolicyBody = {
	/** 책정 수수료 */
	fee?: PlatformFeeInput
	/** 추가 수수료 정책 이름 */
	name?: string
	/** 해당 추가 수수료 정책에 대한 메모 */
	memo?: string
	/** 부가세를 부담할 주체 */
	vatPayer?: PlatformPayer
}
