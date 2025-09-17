/** 빌링키 삭제 요청 주체 */
export type BillingKeyDeleteRequester =
	/** 구매자 */
	| "CUSTOMER"
	/** 관리자 */
	| "ADMIN"
	| string & {}
