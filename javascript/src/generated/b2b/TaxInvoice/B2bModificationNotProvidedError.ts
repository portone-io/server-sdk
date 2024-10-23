/** 세금계산서 수정 입력 정보를 찾을 수 없는 경우 */
export type B2bModificationNotProvidedError = {
	type: "B2B_MODIFICATION_NOT_PROVIDED"
	message?: string
}
