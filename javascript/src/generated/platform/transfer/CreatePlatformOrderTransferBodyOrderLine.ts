import type { CreatePlatformOrderTransferBodyAdditionalFee } from "#generated/platform/transfer/CreatePlatformOrderTransferBodyAdditionalFee"
import type { CreatePlatformOrderTransferBodyDiscount } from "#generated/platform/transfer/CreatePlatformOrderTransferBodyDiscount"
import type { CreatePlatformOrderTransferBodyProduct } from "#generated/platform/transfer/CreatePlatformOrderTransferBodyProduct"

/** 주문 항목 */
export type CreatePlatformOrderTransferBodyOrderLine = {
	/** 상품 */
	product: CreatePlatformOrderTransferBodyProduct
	/**
	 * 상품 수량
	 * (int32)
	 */
	quantity: number
	/** 상품 할인 정보 */
	discounts: CreatePlatformOrderTransferBodyDiscount[]
	/** 상품 추가 수수료 정보 */
	additionalFees: CreatePlatformOrderTransferBodyAdditionalFee[]
}
