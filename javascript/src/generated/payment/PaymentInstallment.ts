/** 할부 정보 */
export type PaymentInstallment = {
	/**
	 * 할부 개월 수
	 * (int32)
	 */
	month: number
	/** 무이자할부 여부 */
	isInterestFree: boolean
}
