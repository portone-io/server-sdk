/** 국세청 연동 상태 */
export type B2bNtsConnectionStatus =
	/** 연동 안 됨 */
	| "NOT_CONNECTED"
	/** 연동 대기 */
	| "PENDING_CONNECT"
	/** 연동 됨 */
	| "CONNECTED"
	/** 연동 해제 대기 */
	| "PENDING_DISCONNECT"
	/** 연동 오류 */
	| "ERROR"
	| string & {}
