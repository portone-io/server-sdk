/**
 * 정산 금액 정보
 *
 * 정산 금액과 정산 금액 계산에 사용된 금액 정보들 입니다.
 */
export type PlatformOrderSettlementAmount = {
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlement: number
	/**
	 * 결제 금액
	 * (int64)
	 */
	payment: number
	/**
	 * 결제 금액 부가세
	 * (int64)
	 */
	paymentVat: number
	/**
	 * 결제 금액 부가세 부담금액
	 *
	 * 참조된 계약의 결제 금액 부가세 감액 여부에 따라 false인 경우 0원, true인 경우 결제 금액 부가세입니다.
	 * (int64)
	 */
	paymentVatBurden: number
	/**
	 * 결제 면세 금액
	 *
	 * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentTaxFree 필드를 사용해주세요.
	 * (int64)
	 */
	taxFree: number
	/**
	 * 결제 공급가액
	 *
	 * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentSupply 필드를 사용해주세요.
	 * (int64)
	 */
	supply: number
	/**
	 * 결제 면세 금액
	 * (int64)
	 */
	paymentTaxFree: number
	/**
	 * 결제 공급가액
	 * (int64)
	 */
	paymentSupply: number
	/**
	 * 주문 금액
	 * (int64)
	 */
	order: number
	/**
	 * 면세 주문 금액
	 * (int64)
	 */
	orderTaxFree: number
	/**
	 * 중개 수수료
	 * (int64)
	 */
	platformFee: number
	/**
	 * 중개 수수료 부가세
	 * (int64)
	 */
	platformFeeVat: number
	/**
	 * 추가 수수료
	 * (int64)
	 */
	additionalFee: number
	/**
	 * 추가 수수료 부가세
	 * (int64)
	 */
	additionalFeeVat: number
	/**
	 * 할인 금액
	 * (int64)
	 */
	discount: number
	/**
	 * 면세 할인 금액
	 * (int64)
	 */
	discountTaxFree: number
	/**
	 * 할인 분담 금액
	 * (int64)
	 */
	discountShare: number
	/**
	 * 면세 할인 분담 금액
	 * (int64)
	 */
	discountShareTaxFree: number
}
