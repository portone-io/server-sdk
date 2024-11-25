import type { PlatformAdditionalFeePolicy } from "./../platform/PlatformAdditionalFeePolicy"
/** 추가 수수료 정책 업데이트 예약 성공 응답 */
export type SchedulePlatformAdditionalFeePolicyResponse = {
	/** 예약된 추가 수수료 정책 */
	scheduledAdditionalFeePolicy: PlatformAdditionalFeePolicy
}
