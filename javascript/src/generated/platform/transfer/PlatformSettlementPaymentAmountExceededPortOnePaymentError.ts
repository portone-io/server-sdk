/** 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우 */
export type PlatformSettlementPaymentAmountExceededPortOnePaymentError = {
	type: "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
	/** (int64) */
	registeredSettlementPaymentAmount: number
	/** (int64) */
	requestSettlementPaymentAmount: number
	/** (int64) */
	portOnePaymentAmount: number
	message?: string
}
