/** 다운로드 할 시트 컬럼 */
export type PlatformBulkPayoutsSheetField =
	/** 지급 실패 금액 */
	| "PAYOUT_FAILED_AMOUNT"
	/** 일괄 지급 이름 */
	| "NAME"
	/** 지급 대기 금액 */
	| "PAYOUT_PREPARED_AMOUNT"
	/** 일괄 지급 방식 */
	| "METHOD"
	/** 지급 성공 금액 */
	| "PAYOUT_SUCCEEDED_AMOUNT"
	/** 지급 성공 건수 */
	| "PAYOUT_SUCCEEDED_COUNT"
	/** 지급 대기 건수 */
	| "PAYOUT_PREPARED_COUNT"
	/** 지급 실패 건수 */
	| "PAYOUT_FAILED_COUNT"
	/** 지급 중단 건수 */
	| "PAYOUT_STOPPED_COUNT"
	/** 일괄 지급 상태 변경 시각 */
	| "STATUS_UPDATED_AT"
	/** 지급 취소 금액 */
	| "PAYOUT_CANCELLED_AMOUNT"
	/** 지급 중단 금액 */
	| "PAYOUT_STOPPED_AMOUNT"
	/** 일괄 지급 생성 시각 */
	| "CREATED_AT"
	/** 총 지급 금액 */
	| "TOTAL_PAYOUT_AMOUNT"
	/** 일괄 지급 상태 */
	| "STATUS"
	/** 일괄 지급 아이디 */
	| "BULK_PAYOUT_ID"
	/** 생성자 아이디 */
	| "CREATOR_ID"
	/** 지급 취소 건수 */
	| "PAYOUT_CANCELLED_COUNT"
