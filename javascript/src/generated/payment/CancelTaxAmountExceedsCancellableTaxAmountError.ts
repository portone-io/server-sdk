/** 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우 */
export type CancelTaxAmountExceedsCancellableTaxAmountError = {
	type: "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT"
	message?: string
}
