import type { PlatformDiscountSharePolicy } from "#generated/platform/PlatformDiscountSharePolicy"

/** 할인 분담 정책 업데이트 예약 성공 응답 */
export type SchedulePlatformDiscountSharePolicyResponse = {
	/** 예약된 할인 분담 정보 */
	scheduledDiscountSharePolicy: PlatformDiscountSharePolicy
}
