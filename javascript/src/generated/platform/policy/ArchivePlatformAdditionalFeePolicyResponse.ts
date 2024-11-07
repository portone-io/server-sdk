import type { PlatformAdditionalFeePolicy } from "./../../platform/PlatformAdditionalFeePolicy"

/** 추가 수수료 정책 보관 성공 응답 */
export type ArchivePlatformAdditionalFeePolicyResponse = {
	/** 보관된 추가 수수료 정책 */
	additionalFeePolicy: PlatformAdditionalFeePolicy
}
