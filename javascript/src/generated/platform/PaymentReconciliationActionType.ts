/** 거래상태 */
export type PaymentReconciliationActionType =
	/** 결제 승인 */
	| "APPROVAL"
	/** 전체 취소 */
	| "FULL_CANCEL"
	/** 부분 취소 */
	| "PARTIAL_CANCEL"
	/** 상태 모르는 취소 */
	| "UNCLASSIFIED_CANCEL"
