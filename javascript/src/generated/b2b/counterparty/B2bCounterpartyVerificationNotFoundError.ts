/**
 * 검증 결과를 찾을 수 없는 경우
 *
 * 사업자 정보 검증 결과를 찾을 수 없습니다.
 */
export type B2bCounterpartyVerificationNotFoundError = {
	type: "B2B_COUNTERPARTY_VERIFICATION_NOT_FOUND"
	message?: string
}
