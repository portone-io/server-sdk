/** 플랫폼 사업자 상태 */
export type PlatformBusinessStatus =
	/** 사업 중 */
	| "IN_BUSINESS"
	/** 폐업 */
	| "CLOSED"
	/** 휴업 */
	| "SUSPENDED"
	| string & {}
