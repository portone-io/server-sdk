/** 정산 건별 옵션이 켜진 플랫폼에서 음수 금액 수기 정산 생성을 시도한 경우 */
export type PlatformNegativeAmountNotAllowedError = {
	type: "PLATFORM_NEGATIVE_AMOUNT_NOT_ALLOWED"
	message?: string
}
