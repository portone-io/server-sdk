/** 국세청에 연동되어 있지 않은 경우 */
export type B2bCounterpartyNtsNotConnectedError = {
	type: "B2B_COUNTERPARTY_NTS_NOT_CONNECTED"
	message?: string
	brn?: string
	counterpartyId?: string
}
