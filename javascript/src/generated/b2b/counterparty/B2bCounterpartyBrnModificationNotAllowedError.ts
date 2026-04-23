/**
 * 사업자등록번호 수정이 허용되지 않는 경우
 *
 * 거래처의 사업자등록번호는 수정할 수 없습니다.
 */
export type B2bCounterpartyBrnModificationNotAllowedError = {
	type: "B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED"
	message?: string
}
