/** 빌링키 다건 조회 시, 시각 범위를 적용할 필드 */
export type BillingKeyTimeRangeField =
	/** 발급 요청 시각 */
	| "REQUESTED_AT"
	/** 발급 완료 시각 */
	| "ISSUED_AT"
	/** 삭제 완료 시각 */
	| "DELETED_AT"
	/**
	 * 상태 변경 시각
	 *
	 * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
	 */
	| "STATUS_TIMESTAMP"
	| string & {}
