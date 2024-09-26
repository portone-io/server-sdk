/** 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우 */
export type PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError = {
	type: "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
	/** (int64) */
	registeredSettlementSupplyWithVatAmount: number
	/** (int64) */
	requestSettlementSupplyWithVatAmount: number
	/** (int64) */
	portOneSupplyWithVatAmount: number
	message?: string
}
