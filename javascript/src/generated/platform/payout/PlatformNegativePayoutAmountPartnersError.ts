/** 지급 금액의 총합이 음수인 파트너가 존재하는 경우 */
export type PlatformNegativePayoutAmountPartnersError = {
	type: "PLATFORM_CURRENCY_NOT_SUPPORTED"
	message?: string
}
