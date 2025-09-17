/** 결제 취소 요청 주체 */
export type CancelRequester =
	/** 구매자 */
	| "CUSTOMER"
	/** 관리자 */
	| "ADMIN"
	| string & {}
