/**
 * 필수 입력 항목이 누락된 경우
 *
 * 거래처 생성/수정 시 필수 입력 항목이 누락되었습니다.
 */
export type B2bCounterpartyMissingRequiredFieldsError = {
	type: "B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS"
	message?: string
}
