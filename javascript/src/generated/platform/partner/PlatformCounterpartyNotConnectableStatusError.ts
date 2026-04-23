/** 파트너 거래처 연동 상태가 연동 가능한 상태가 아닌 경우 */
export type PlatformCounterpartyNotConnectableStatusError = {
	type: "PLATFORM_COUNTERPARTY_NOT_CONNECTABLE_STATUS"
	message?: string
}
