/** 현금영수증 발급 가능 결제 수단 */
export type IssueCashReceiptPaymentMethodType =
	/** 계좌이체 */
	| "TRANSFER"
	/** 가상계좌 */
	| "VIRTUAL_ACCOUNT"
	| string & {}
