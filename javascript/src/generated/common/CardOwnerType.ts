/** 카드 소유주 유형 */
export type CardOwnerType =
	/** 개인 */
	| "PERSONAL"
	/** 법인 */
	| "CORPORATE"
	| string & {}
