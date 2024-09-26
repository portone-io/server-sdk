/** 지급 가능한 정산일 리스트 조회 성공 응답 정보 */
export type GetPlatformPayableSettlementDatesResponse = {
	/** IN_PROCESS, SETTLED 상태의 Transfer가 등록되어 있는 정산일 리스트 */
	settlementDates: string[]
}
