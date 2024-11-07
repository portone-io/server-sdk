import type { CreatePlatformOrderCancelTransferBodyOrderDetailAll } from "./../../platform/transfer/CreatePlatformOrderCancelTransferBodyOrderDetailAll"
import type { CreatePlatformOrderCancelTransferBodyOrderLine } from "./../../platform/transfer/CreatePlatformOrderCancelTransferBodyOrderLine"

/**
 * 주문 취소 정보
 *
 * orderAmount, orderLines, all 중에서 하나만 입력하여야 합니다.
 */
export type CreatePlatformOrderCancelTransferBodyOrderDetail = {
	/**
	 * 주문 취소 금액
	 * (int64)
	 */
	orderAmount?: number
	/** 주문 취소 항목 리스트 */
	orderLines?: CreatePlatformOrderCancelTransferBodyOrderLine[]
	/** 전체 금액 취소 */
	all?: CreatePlatformOrderCancelTransferBodyOrderDetailAll
}
