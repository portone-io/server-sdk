/** 계좌 이체 상태 */
export type PlatformAccountTransferStatus =
	/** 대기 */
	| "PREPARED"
	/** 예약 */
	| "SCHEDULED"
	/** 취소 */
	| "CANCELLED"
	/** 중단 */
	| "STOPPED"
	/** 처리 중 */
	| "PROCESSING"
	/** 비동기 처리 중 */
	| "ASYNC_PROCESSING"
	/** 성공 */
	| "SUCCEEDED"
	/** 실패 */
	| "FAILED"
	| string & {}
