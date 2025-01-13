/** 플랫폼 계좌 상태 */
export type PlatformAccountStatus =
	/** 계좌 인증 완료됨 */
	| "VERIFIED"
	/** 계좌주 불일치 */
	| "VERIFY_FAILED"
	/** 계좌 인증 오류 */
	| "VERIFY_ERROR"
	/** 계좌 인증 안됨 */
	| "NOT_VERIFIED"
	/** 알 수 없는 상태 */
	| "UNKNOWN"
	| string & {}
