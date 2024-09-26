import type { PlatformContract } from "#generated/platform/PlatformContract"

/** 계약 예약 업데이트 재설정 성공 응답 */
export type ReschedulePlatformContractResponse = {
	/** 예약된 계약 정보 */
	scheduledContract: PlatformContract
}
