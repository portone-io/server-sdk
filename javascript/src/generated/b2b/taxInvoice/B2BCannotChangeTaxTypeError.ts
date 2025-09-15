/** 세금계산서 과세 유형을 수정할 수 없는 경우 */
export type B2BCannotChangeTaxTypeError = {
	type: "B2B_CANNOT_CHANGE_TAX_TYPE"
	message?: string
}
