import type { PlatformAdditionalFeePolicy } from "./../platform/PlatformAdditionalFeePolicy"
/** 추가 수수료 정책 예약 업데이트 재설정 성공 응답 */
export type ReschedulePlatformAdditionalFeePolicyResponse = {
	/** 예약된 추가 수수료 정책 */
	scheduledAdditionalFeePolicy: PlatformAdditionalFeePolicy
}
