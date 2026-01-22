/** 간소화된 결제수단 목록 */
export type SimplifiedPaymentMethodType =
	/** 신용카드/체크카드 */
	| "CARD"
	/** 가상계좌 */
	| "VIRTUAL_ACCOUNT"
	/** 계좌이체 */
	| "TRANSFER"
	/** 머니 */
	| "CHARGE"
	/** 모바일 */
	| "MOBILE"
	/** 포인트 */
	| "POINT"
	/** 기타 */
	| "ETC"
	| string & {}
