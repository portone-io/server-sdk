/** 입력 시 발급 유형 */
export type CashReceiptInputType =
	/** 소득공제용 */
	| "PERSONAL"
	/** 지출증빙용 */
	| "CORPORATE"
	/**
	 * 미발행
	 *
	 * PG사 설정에 따라 PG사가 자동으로 자진발급 처리할 수 있습니다.
	 */
	| "NO_RECEIPT"
	| string & {}
