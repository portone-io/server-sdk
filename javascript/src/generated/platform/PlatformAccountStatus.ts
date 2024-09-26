/** 플랫폼 계좌 상태 */
export type PlatformAccountStatus =
	/** 계좌 인증 안됨 */
	| "NOT_VERIFIED"
	/** 계좌 인증 만료됨 */
	| "EXPIRED"
	/** 계좌 인증 실패함 */
	| "VERIFY_FAILED"
	/** 계좌 인증 완료됨 */
	| "VERIFIED"
	/** 계좌 인증 중 */
	| "VERIFYING"
	/** 알 수 없는 상태 */
	| "UNKNOWN"
