import type { CreatePlatformOrderTransferBodyOrderLine } from "./../../platform/transfer/CreatePlatformOrderTransferBodyOrderLine"

/**
 * 주문 정보
 *
 * 주문 금액 또는 주문 항목 하나만 입력 가능합니다.
 */
export type CreatePlatformOrderTransferBodyOrderDetail = {
	/**
	 * 주문 금액
	 * (int64)
	 */
	orderAmount?: number
	/** 주문 항목 리스트 */
	orderLines?: CreatePlatformOrderTransferBodyOrderLine[]
}
