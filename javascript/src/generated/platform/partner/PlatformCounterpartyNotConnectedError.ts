/** 파트너가 거래처로 연동 되어있지 않은 경우 */
export type PlatformCounterpartyNotConnectedError = {
	type: "PLATFORM_COUNTERPARTY_NOT_CONNECTED"
	message?: string
}
