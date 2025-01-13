/** 플랫폼 파트너 사업자 상태 */
export type PlatformPartnerBusinessStatus =
	/** 조회 되지 않음 */
	| "NOT_VERIFIED"
	/** 조회 오류 */
	| "VERIFY_ERROR"
	/** 대응되는 사업자 없음 */
	| "NOT_FOUND"
	/** 사업 중 */
	| "IN_BUSINESS"
	/** 폐업 */
	| "CLOSED"
	/** 휴업 */
	| "SUSPENDED"
	| string & {}
