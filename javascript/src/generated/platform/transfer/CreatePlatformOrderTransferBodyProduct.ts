/** 상품 */
export type CreatePlatformOrderTransferBodyProduct = {
	/** 상품 아이디 */
	id: string
	/** 상품 이름 */
	name: string
	/**
	 * 상품 금액
	 * (int64)
	 */
	amount: number
	/**
	 * 상품 면세 금액
	 * (int64)
	 */
	taxFreeAmount?: number
	/** 태그 */
	tag?: string
}
