export type AmountExceededType =
	/** 할인금액이 주문금액을 초과 */
	| "DISCOUNT_THAN_ORDER"
	/** 면세 할인금액이 할인금액을 초과 */
	| "DISCOUNT_TAX_FREE_THAN_DISCOUNT"
	/** 면세 할인금액이 면세 주문금액을 초과 */
	| "DISCOUNT_TAX_FREE_THAN_ORDER_TAX_FREE"
	/** 면세 결제금액이 결제금액을 초과 */
	| "PAYMENT_TAX_FREE_THAN_PAYMENT"
