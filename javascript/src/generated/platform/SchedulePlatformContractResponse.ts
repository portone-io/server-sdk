import type { PlatformContract } from "#generated/platform/PlatformContract"

/** 계약 업데이트 예약 성공 응답 */
export type SchedulePlatformContractResponse = {
	/** 예약된 계약 정보 */
	scheduledContract: PlatformContract
}
