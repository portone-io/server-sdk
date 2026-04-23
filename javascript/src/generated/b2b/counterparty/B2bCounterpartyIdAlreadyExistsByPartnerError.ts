/**
 * 파트너 연동으로 생성된 거래처 ID가 이미 사용중인 경우
 *
 * 파트너 연동으로 생성된 거래처 ID는 재사용할 수 없습니다.
 */
export type B2bCounterpartyIdAlreadyExistsByPartnerError = {
	type: "B2B_COUNTERPARTY_ID_ALREADY_EXISTS_BY_PARTNER"
	message?: string
}
