/**
 * 정률 수수료
 *
 * 총 금액에 정해진 비율을 곱한 만큼의 수수료를 책정합니다.
 */
export type PlatformFixedRateFee = {
	type: "FIXED_RATE"
	/**
	 * 수수료율
	 *
	 * 총 금액 대비 수수료 비율을 의미하며, 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수입니다. `총 금액 * rate * 10^5` (`rate * 10^3 %`) 만큼 수수료를 책정합니다.
	 * (int32)
	 */
	rate: number
}
