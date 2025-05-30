/** 계좌 이체 상태 */
export type Status =
	/** 처리 중 */
	| "PROCESSING"
	/** 비동기 처리 중 */
	| "ASYNC_PROCESSING"
	/** 성공 */
	| "SUCCEEDED"
	/** 실패 */
	| "FAILED"
	| string & {}
