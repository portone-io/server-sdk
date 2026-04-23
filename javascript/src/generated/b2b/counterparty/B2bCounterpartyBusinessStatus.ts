/** 거래처 휴폐업 상태 */
export type B2bCounterpartyBusinessStatus =
	/** 미조회 */
	| "UNKNOWN"
	/** 영업중 */
	| "IN_BUSINESS"
	/** 폐업 */
	| "CLOSED"
	/** 휴업 */
	| "SUSPENDED"
	/** 사업체 미등록 */
	| "NOT_FOUND"
	/**
	 * 조회 대기
	 *
	 * 일괄 등록 시 조회 대기 상태입니다.
	 */
	| "CHECK_PENDING"
	/** 조회 실패 */
	| "CHECK_FAILED"
	| string & {}
