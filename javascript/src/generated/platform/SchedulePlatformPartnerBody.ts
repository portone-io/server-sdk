import type { UpdatePlatformPartnerBody } from "./../platform/UpdatePlatformPartnerBody"

/** 파트너 업데이트 예약을 위한 입력 정보 */
export type SchedulePlatformPartnerBody = {
	/** 반영할 업데이트 내용 */
	update: UpdatePlatformPartnerBody
	/**
	 * 업데이트 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
