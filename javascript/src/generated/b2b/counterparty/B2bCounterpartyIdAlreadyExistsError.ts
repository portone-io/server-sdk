/** 거래처 ID가 이미 사용중인 경우 */
export type B2bCounterpartyIdAlreadyExistsError = {
	type: "B2B_COUNTERPARTY_ID_ALREADY_EXISTS"
	message?: string
}
