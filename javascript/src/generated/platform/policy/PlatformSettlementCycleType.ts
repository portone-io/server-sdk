/** 플랫폼 정산 주기 계산 방식 */
export type PlatformSettlementCycleType =
	/** 매일 정산 */
	| "DAILY"
	/** 매주 정해진 요일에 정산 */
	| "WEEKLY"
	/** 매월 정해진 날(일)에 정산 */
	| "MONTHLY"
	/** 정해진 날짜(월, 일)에 정산 */
	| "MANUAL_DATES"
