/** 상품 유형 */
export type PaymentProductType =
	/** 실물 상품 */
	| "PHYSICAL"
	/**
	 * 디지털 상품
	 *
	 * 서비스, 온라인 상품 등 실물이 존재하지 않는 무형의 상품을 의미합니다.
	 */
	| "DIGITAL"
	| string & {}
