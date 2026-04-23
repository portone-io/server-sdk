/** 거래처가 존재하지 않는 경우 */
export type B2bCounterpartyNotFoundError = {
	type: "B2B_COUNTERPARTY_NOT_FOUND"
	message?: string
	counterpartyId?: string
}
