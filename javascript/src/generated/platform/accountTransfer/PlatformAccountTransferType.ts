/** 계좌 이체 유형 */
export type PlatformAccountTransferType =
	/** 충전 */
	| "DEPOSIT"
	/** 파트너 정산 송금 */
	| "WITHDRAWAL_PARTNER_PAYOUT"
	/** 송금 */
	| "WITHDRAWAL_REMIT"
	| string & {}
