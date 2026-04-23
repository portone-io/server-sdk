/** 페이먼트월 배송 유형 */
export type PaymentwallDeliveryType =
	/** 디지털 */
	| "DIGITAL"
	/** 실물 */
	| "PHYSICAL"
	| string & {}
