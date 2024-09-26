/** 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우 */
export type SumOfPartsExceedsTotalAmountError = {
	type: "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT"
	message?: string
}
