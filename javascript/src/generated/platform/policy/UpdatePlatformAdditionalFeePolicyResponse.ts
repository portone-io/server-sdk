import type { PlatformAdditionalFeePolicy } from "./../../platform/PlatformAdditionalFeePolicy"

/** 추가 수수료 정책 업데이트 성공 응답 */
export type UpdatePlatformAdditionalFeePolicyResponse = {
	/** 업데이트된 추가 수수료 정책 */
	additionalFeePolicy: PlatformAdditionalFeePolicy
}
