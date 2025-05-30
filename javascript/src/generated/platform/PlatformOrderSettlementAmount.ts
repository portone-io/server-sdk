import type { PlatformUserDefinedFormulaResults } from "./../platform/PlatformUserDefinedFormulaResults"
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
	 * 정산 면세 금액
	 * (int64)
	 */
	settlementTaxFree: number
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
	/** 사용자 정의 수식 결과 */
	userDefinedFormulas: PlatformUserDefinedFormulaResults
}
