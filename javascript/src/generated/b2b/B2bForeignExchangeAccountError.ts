/** 계좌 정보 조회가 불가능한 외화 계좌인 경우 */
export type B2bForeignExchangeAccountError = {
	type: "B2B_FOREIGN_EXCHANGE_ACCOUNT"
	message?: string
}
