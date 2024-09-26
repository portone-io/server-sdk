import type { PlatformPartnerDashboardCount } from "#generated/platform/PlatformPartnerDashboardCount"

/** 파트너 현황 조회 성공 응답 */
export type PlatformPartnerDashboard = {
	/** 전체 파트너 현황 */
	totalPartner: PlatformPartnerDashboardCount
	/** 정산 예정인 파트너 현황 */
	upcomingSettledPartner: PlatformPartnerDashboardCount
	/**
	 * 예정된 정산일
	 *
	 * 정산이 예정되어 있지 않은 경우 값이 주어지지 않습니다.
	 */
	upcomingSettlementDate?: string
}
