import type { B2bTaxInvoiceSummary } from "./../../b2b/taxInvoice/B2bTaxInvoiceSummary"
import type { PageInfo } from "./../../common/PageInfo"
/** 세금계산서 다건 조회 성공 응답 */
export type GetB2bTaxInvoicesResponse = {
	/** 조회된 세금계산서 목록 */
	items: B2bTaxInvoiceSummary[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
