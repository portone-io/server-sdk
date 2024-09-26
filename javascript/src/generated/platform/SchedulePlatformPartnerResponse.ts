import type { PlatformPartner } from "#generated/platform/PlatformPartner"

/** 파트너 업데이트 예약 성공 응답 */
export type SchedulePlatformPartnerResponse = {
	/** 예약된 파트너 정보 */
	scheduledPartner: PlatformPartner
}
