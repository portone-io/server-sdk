/** 현금영수증 정렬 기준 */
export type CashReceiptSortBy =
	/** 발급 시각 */
	| "ISSUED_AT"
	/** 취소 시각 */
	| "CANCELLED_AT"
	/**
	 * 상태 변경 시각
	 *
	 * 발급 상태의 경우 ISSUED_AT, 취소 상태의 경우 CANCELLED_AT
	 */
	| "STATUS_UPDATED_AT"
	| string & {}
