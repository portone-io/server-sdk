/** 할인 정보 */
export type CreatePlatformOrderCancelTransferBodyDiscount = {
	/** 할인 분담 정책 아이디 */
	sharePolicyId: string
	/**
	 * 할인 금액
	 * (int64)
	 */
	amount: number
	/**
	 * 면세 할인 금액
	 * (int64)
	 */
	taxFreeAmount?: number
}
