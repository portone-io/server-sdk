import type { UpdatePlatformAdditionalFeePolicyBody } from "./../platform/UpdatePlatformAdditionalFeePolicyBody"

/** 추가 수수료 정책 업데이트 예약을 위한 입력 정보 */
export type SchedulePlatformAdditionalFeePolicyBody = {
	/** 반영할 업데이트 내용 */
	update: UpdatePlatformAdditionalFeePolicyBody
	/**
	 * 업데이트 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
