/** 제공자 */
export type PlatformBankAccountProvider =
	/** 하이픈 데이터 */
	| "HYPHEN_DATA"
	/** 하이픈 펌뱅킹 */
	| "HYPHEN_FIRM"
	/** 더즌 */
	| "DOZN"
	/** 모의 */
	| "MOCK"
	| string & {}
