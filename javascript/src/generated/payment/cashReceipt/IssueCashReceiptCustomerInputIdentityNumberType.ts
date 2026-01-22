/** 현금영수증 발급 시 고객 식별 정보 유형 */
export type IssueCashReceiptCustomerInputIdentityNumberType =
	/** 휴대전화번호 */
	| "PHONE"
	/** 카드번호 */
	| "CARD"
	/** 사업자등록번호 */
	| "BUSINESS"
	| string & {}
