import type { PaymentTextSearchField } from "./../payment/PaymentTextSearchField"

/** 통합검색 입력 정보 */
export type PaymentTextSearch = {
	field: PaymentTextSearchField
	value: string
}
