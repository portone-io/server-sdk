/** 본인인증 상태 */
export type IdentityVerificationStatus =
	/** 요청 상태 */
	| "READY"
	/** 완료 상태 */
	| "VERIFIED"
	/** 실패 상태 */
	| "FAILED"
	| string & {}
