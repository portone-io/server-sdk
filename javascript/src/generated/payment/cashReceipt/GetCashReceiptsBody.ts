import type { CashReceiptFilterInput } from "./../../payment/cashReceipt/CashReceiptFilterInput"
import type { CashReceiptSortInput } from "./../../payment/cashReceipt/CashReceiptSortInput"
import type { PageInput } from "./../../common/PageInput"
/** 현금영수증 다건 조회를 위한 입력 정보 */
export type GetCashReceiptsBody = {
	/**
	 * 요청할 페이지 정보
	 *
	 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
	 */
	page?: PageInput
	/**
	 * 정렬 조건
	 *
	 * 미 입력 시 sortBy: ISSUED_AT, sortOrder: DESC 으로 기본값이 적용됩니다.
	 */
	sort?: CashReceiptSortInput
	/** 조회할 현금영수증 조건 필터 */
	filter?: CashReceiptFilterInput
}
