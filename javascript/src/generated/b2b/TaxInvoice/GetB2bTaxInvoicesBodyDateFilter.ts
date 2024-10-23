import type { B2bSearchDateType } from "#generated/b2b/TaxInvoice/B2bSearchDateType"
import type { DateRangeOption } from "#generated/b2b/TaxInvoice/DateRangeOption"

/** 조회 기간 필터 */
export type GetB2bTaxInvoicesBodyDateFilter = {
	/**
	 * 조회 기간 기준
	 *
	 * 미입력시 기본값은 등록일(`REGISTER`)로 설정됩니다.
	 */
	dateType?: B2bSearchDateType
	/**
	 * 조회 기간
	 *
	 * 미입력시 `dateRange.from`의 기본값은 한 달 이전, `dateRange.until`의 기본값은 현재 일자로 설정됩니다.
	 */
	dateRange?: DateRangeOption[]
}
