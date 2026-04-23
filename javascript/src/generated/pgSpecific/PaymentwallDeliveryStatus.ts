/** 페이먼트월 배송 상태 */
export type PaymentwallDeliveryStatus =
	/** 주문 접수 */
	| "ORDER_PLACED"
	/** 배송 중 */
	| "ORDER_SHIPPED"
	/** 배송 완료 */
	| "DELIVERED"
	| string & {}
