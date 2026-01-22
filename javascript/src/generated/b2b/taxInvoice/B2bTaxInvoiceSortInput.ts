import type { B2bTaxInvoiceSortBy } from "./../../b2b/taxInvoice/B2bTaxInvoiceSortBy"
import type { SortOrder } from "./../../common/SortOrder"
/** 세금계산서 다건 조회 시 정렬 조건 */
export type B2bTaxInvoiceSortInput = {
	/** 정렬 기준 */
	by?: B2bTaxInvoiceSortBy
	/** 정렬 방식 */
	order?: SortOrder
}
