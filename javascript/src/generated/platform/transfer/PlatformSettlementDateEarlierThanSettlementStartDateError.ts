/** 정산일이 정산 시작일보다 빠른 경우 */
export type PlatformSettlementDateEarlierThanSettlementStartDateError = {
	type: "PLATFORM_SETTLEMENT_DATE_EARLIER_THAN_SETTLEMENT_START_DATE"
	message?: string
	/**
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementStartDate: string
	/**
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	settlementDate: string
}
