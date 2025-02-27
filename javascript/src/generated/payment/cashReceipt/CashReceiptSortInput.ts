import type { CashReceiptSortBy } from "./../../payment/cashReceipt/CashReceiptSortBy"
import type { SortOrder } from "./../../common/SortOrder"
/** 현금영수증 다건 조회 시 정렬 조건 */
export type CashReceiptSortInput = {
	/**
	 * 정렬 기준 필드
	 *
	 * 어떤 필드를 기준으로 정렬할 지 결정합니다. 비워서 보낼 경우, ISSUED_AT이 기본값으로 설정됩니다.
	 */
	by?: CashReceiptSortBy
	/**
	 * 정렬 순서
	 *
	 * 어떤 순서로 정렬할 지 결정합니다. 비워서 보낼 경우, DESC(내림차순)가 기본값으로 설정됩니다.
	 */
	order?: SortOrder
}
