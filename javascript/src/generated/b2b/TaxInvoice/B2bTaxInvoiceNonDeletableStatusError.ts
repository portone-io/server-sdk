/**
 * 세금계산서가 삭제 가능한 상태가 아닌 경우
 *
 * 삭제 가능한 상태는 `DRAFTED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
 */
export type B2bTaxInvoiceNonDeletableStatusError = {
	type: "B2B_TAX_INVOICE_NON_DELETABLE_STATUS"
	message?: string
}
