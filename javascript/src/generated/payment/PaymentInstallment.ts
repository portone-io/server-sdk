/** 할부 정보 */
export type PaymentInstallment = {
	/**
	 * 할부 개월 수
	 * (int32)
	 */
	month: number
	/** 무이자할부 여부 */
	isInterestFree: boolean
	/**
	 * 상점 부담 무이자할부 여부
	 *
	 * 정보 필요시 포트원과 협의해 주세요.
	 */
	isInterestFreeFromMerchant?: boolean
}
