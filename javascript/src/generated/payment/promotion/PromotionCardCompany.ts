/** 프로모션 적용 가능한 카드사 */
export type PromotionCardCompany =
	/** 우리카드 */
	| "WOORI_CARD"
	/** BC카드 */
	| "BC_CARD"
	/** 삼성카드 */
	| "SAMSUNG_CARD"
	/** 신한카드 */
	| "SHINHAN_CARD"
	/** 현대카드 */
	| "HYUNDAI_CARD"
	/** 롯데카드 */
	| "LOTTE_CARD"
	/** NH카드 */
	| "NH_CARD"
	/** 하나카드 */
	| "HANA_CARD"
	/** 국민카드 */
	| "KOOKMIN_CARD"
	| string & {}
