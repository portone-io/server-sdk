import type { CreatePlatformOrderCancelTransferBodyDiscount } from "#generated/platform/transfer/CreatePlatformOrderCancelTransferBodyDiscount"

/** 주문 취소 항목 리스트 */
export type CreatePlatformOrderCancelTransferBodyOrderLine = {
	/** 상품 아이디 */
	productId: string
	/**
	 * 상품 수량
	 * (int32)
	 */
	quantity: number
	/** 상품 할인 정보 */
	discounts: CreatePlatformOrderCancelTransferBodyDiscount[]
}
