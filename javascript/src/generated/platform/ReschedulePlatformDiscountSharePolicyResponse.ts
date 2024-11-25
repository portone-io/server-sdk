import type { PlatformDiscountSharePolicy } from "./../platform/PlatformDiscountSharePolicy"
/** 할인 분담 정책 예약 업데이트 재설정 성공 응답 */
export type ReschedulePlatformDiscountSharePolicyResponse = {
	/** 예약된 할인 분담 정보 */
	scheduledDiscountSharePolicy: PlatformDiscountSharePolicy
}
