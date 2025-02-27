/** 현금영수증 다건 조회 시, 시각 범위를 적용할 필드 */
export type CashReceiptTimeRangeField =
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
