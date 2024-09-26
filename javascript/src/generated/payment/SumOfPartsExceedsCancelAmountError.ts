/** 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우 */
export type SumOfPartsExceedsCancelAmountError = {
	type: "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT"
	message?: string
}
