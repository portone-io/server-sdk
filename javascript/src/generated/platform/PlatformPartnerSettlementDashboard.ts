import type { PlatformPartnerSettlementDashboardCurrencyStat } from "#generated/platform/PlatformPartnerSettlementDashboardCurrencyStat"

/** 정산내역 대시보드 */
export type PlatformPartnerSettlementDashboard = {
	/** 정산 통화별 정산내역 통계 리스트 */
	currencyStats: PlatformPartnerSettlementDashboardCurrencyStat[]
}
