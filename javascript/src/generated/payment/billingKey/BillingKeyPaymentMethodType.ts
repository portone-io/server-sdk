/** 빌링키 결제 수단 */
export type BillingKeyPaymentMethodType =
	/** 카드 */
	| "CARD"
	/** 모바일 */
	| "MOBILE"
	/** 간편 결제 */
	| "EASY_PAY"
	/** 계좌 이체 */
	| "TRANSFER"
