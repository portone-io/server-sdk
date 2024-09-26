/** 플랫폼 정산 기준일 */
export type PlatformSettlementCycleDatePolicy =
	/** 공휴일 전 영업일 */
	| "HOLIDAY_BEFORE"
	/** 공휴일 후 영업일 */
	| "HOLIDAY_AFTER"
	/** 달력일 */
	| "CALENDAR_DAY"
