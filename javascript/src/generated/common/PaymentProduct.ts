/** 상품 정보 */
export type PaymentProduct = {
	/**
	 * 상품 고유 식별자
	 *
	 * 고객사가 직접 부여한 식별자입니다.
	 */
	id: string
	/** 상품명 */
	name: string
	/**
	 * 상품 태그
	 *
	 * 카테고리 등으로 활용될 수 있습니다.
	 */
	tag?: string
	/** 상품 코드 */
	code?: string
	/**
	 * 상품 단위가격
	 * (int64)
	 */
	amount: number
	/**
	 * 주문 수량
	 * (int32)
	 */
	quantity: number
}
