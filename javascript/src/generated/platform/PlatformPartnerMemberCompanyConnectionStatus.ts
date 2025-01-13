/** 플랫폼 파트너 연동 사업자 연결 상태 */
export type PlatformPartnerMemberCompanyConnectionStatus =
	/** 연결되지 않음 */
	| "NOT_CONNECTED"
	/** 연결 대기 */
	| "CONNECT_PENDING"
	/** 연결됨 */
	| "CONNECTED"
	/** 연결 실패 */
	| "CONNECT_FAILED"
	/** 연결 해제 대기 */
	| "DISCONNECT_PENDING"
	| string & {}
