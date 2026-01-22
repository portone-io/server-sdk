/** 결제 건의 대사 상태 */
export type PaymentReconciliationStatus =
	/** 대사 매칭 성공 상태 */
	| "MATCHED"
	/** 대사 매칭 실패 상태 */
	| "NOT_MATCHED"
	/** 대사 불가능 상태 */
	| "INCOMPARABLE"
	/** PG사 결제 정보가 수집되지 않은 상태 */
	| "NOT_COLLECTED"
	| string & {}
