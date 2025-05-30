/** 계좌 이체 유형 */
export type PlatformAccountTransferType =
	/** 입금 */
	| "DEPOSIT"
	/** 출금 */
	| "WITHDRAWAL"
	| string & {}
