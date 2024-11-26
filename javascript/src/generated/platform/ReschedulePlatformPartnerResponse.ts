import type { PlatformPartner } from "./../platform/PlatformPartner"
/** 파트너 예약 업데이트 재설정 성공 응답 */
export type ReschedulePlatformPartnerResponse = {
	/** 예약된 파트너 정보 */
	scheduledPartner: PlatformPartner
}
