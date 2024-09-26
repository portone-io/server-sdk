import type { PlatformAdditionalFeePolicy } from "#generated/platform/PlatformAdditionalFeePolicy"

/** 플랫폼 생성 성공 응답 정보 */
export type CreatePlatformAdditionalFeePolicyResponse = {
	/** 생성된 추가 수수료 정책 */
	additionalFeePolicy: PlatformAdditionalFeePolicy
}
