/** 정산 유형 */
export type PlatformPartnerSettlementType =
	/** 수동 정산 */
	| "MANUAL"
	/** 주문 정산 */
	| "ORDER"
	/** 주문 취소 정산 */
	| "ORDER_CANCEL"
