import type { GetB2bTaxInvoicesBodyFilter } from "./../../b2b/taxInvoice/GetB2bTaxInvoicesBodyFilter"
import type { TaxInvoicesSheetField } from "./../../b2b/taxInvoice/TaxInvoicesSheetField"
export type DownloadB2bTaxInvoicesSheetBody = {
	filter?: GetB2bTaxInvoicesBodyFilter
	/** 다운로드 할 시트 컬럼 */
	fields?: TaxInvoicesSheetField[]
	test?: boolean
}
