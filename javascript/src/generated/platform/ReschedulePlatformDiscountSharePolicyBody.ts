import type { UpdatePlatformDiscountSharePolicyBody } from "#generated/platform/UpdatePlatformDiscountSharePolicyBody"

/** 할인 분담 정책 예약 업데이트 재설정을 위한 입력 정보 */
export type ReschedulePlatformDiscountSharePolicyBody = {
	/** 반영할 업데이트 내용 */
	update: UpdatePlatformDiscountSharePolicyBody
	/**
	 * 업데이트 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
