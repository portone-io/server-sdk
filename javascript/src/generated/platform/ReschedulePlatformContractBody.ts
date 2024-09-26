import type { UpdatePlatformContractBody } from "#generated/platform/UpdatePlatformContractBody"

/** 계약 예약 업데이트 재설정을 위한 입력 정보 */
export type ReschedulePlatformContractBody = {
	/** 반영할 업데이트 내용 */
	update: UpdatePlatformContractBody
	/**
	 * 업데이트 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
