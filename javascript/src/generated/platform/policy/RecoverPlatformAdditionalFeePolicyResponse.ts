import type { PlatformAdditionalFeePolicy } from "./../../platform/PlatformAdditionalFeePolicy"

/** 추가 수수료 정책 복원 성공 응답 */
export type RecoverPlatformAdditionalFeePolicyResponse = {
	/** 복원된 추가 수수료 정책 */
	additionalFeePolicy: PlatformAdditionalFeePolicy
}
