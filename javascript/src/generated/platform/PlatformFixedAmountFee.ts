/**
 * 정액 수수료
 *
 * 총 금액에 무관하게 정해진 수수료 금액을 책정합니다.
 */
export type PlatformFixedAmountFee = {
	type: "FIXED_AMOUNT"
	/**
	 * 고정된 수수료 금액
	 * (int64)
	 */
	amount: number
}
