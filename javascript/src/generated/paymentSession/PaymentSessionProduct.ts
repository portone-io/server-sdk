/** 결제 세션 주문 항목 */
export type PaymentSessionProduct = {
	/** 항목 아이디 */
	id?: string
	/** 상품 이름 */
	name: string
	/** 상품 코드 */
	code?: string
	/**
	 * 상품 단가
	 * (int64)
	 */
	unitPrice: number
	/**
	 * 상품 수량
	 * (int32)
	 */
	quantity: number
	/**
	 * 제공 시작일
	 *
	 * 구독 등 제공 기간이 있는 상품의 경우 입력하세요.
	 * (yyyy-MM-dd)
	 */
	startDate?: string
	/**
	 * 제공 종료일
	 *
	 * 구독 등 제공 기간이 있는 상품의 경우 입력하세요.
	 * (yyyy-MM-dd)
	 */
	endDate?: string
	/** 판매 링크 */
	url?: string
	/** 네이버페이 카테고리 타입 */
	nPayCategoryType?: string
	/** 네이버페이 카테고리 아이디 */
	nPayCategoryId?: string
	/** 네이버페이 상품 식별자 */
	nPayUid?: string
}
