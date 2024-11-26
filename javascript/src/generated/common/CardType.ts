/** 카드 유형 */
export type CardType =
	/** 신용카드 */
	| "CREDIT"
	/** 체크카드 */
	| "DEBIT"
	/** 기프트카드 */
	| "GIFT"
	| string & {}
