/** 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우 */
export type PlatformSettlementTaxFreeAmountExceededPortOnePaymentError = {
	type: "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
	/** (int64) */
	registeredSettlementTaxFreeAmount: number
	/** (int64) */
	requestSettlementTaxFreeAmount: number
	/** (int64) */
	portOneTaxFreeAmount: number
	message?: string
}
