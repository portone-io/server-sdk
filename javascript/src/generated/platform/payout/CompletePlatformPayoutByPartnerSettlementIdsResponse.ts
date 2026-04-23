/** 일괄 지급 완료 처리 결과 */
export type CompletePlatformPayoutByPartnerSettlementIdsResponse = {
	bulkPayoutId?: string
	bulkPayoutGraphqlId?: string
	/** (int32) */
	payoutCount: number
	/** (int32) */
	partnerSettlementCount: number
}
