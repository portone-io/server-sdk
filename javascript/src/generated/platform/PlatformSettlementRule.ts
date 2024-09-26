/** 플랫폼 정산건 처리 방식에 관한 규칙 */
export type PlatformSettlementRule = {
	/** paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부 */
	supportsMultipleOrderTransfersPerPartner: boolean
	/** 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부 */
	adjustSettlementDateAfterHolidayIfEarlier: boolean
	/** 지급 금액에서 원천징수세 차감 여부 */
	subtractWhtInPayoutAmount: boolean
}
