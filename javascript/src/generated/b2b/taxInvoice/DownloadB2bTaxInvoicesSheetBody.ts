import type { B2bTaxInvoiceSortInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceSortInput"
import type { GetB2bTaxInvoicesBodyFilter } from "./../../b2b/taxInvoice/GetB2bTaxInvoicesBodyFilter"
import type { TaxInvoicesSheetField } from "./../../b2b/taxInvoice/TaxInvoicesSheetField"
export type DownloadB2bTaxInvoicesSheetBody = {
	filter?: GetB2bTaxInvoicesBodyFilter
	/** 다운로드 할 시트 컬럼 */
	fields?: TaxInvoicesSheetField[]
	test?: boolean
	/**
	 * 정렬 조건
	 *
	 * 미입력 시 상태 업데이트 일시 내림차순 정렬됩니다.
	 */
	sort?: B2bTaxInvoiceSortInput
}
