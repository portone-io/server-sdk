/**
 * 파트너 연동 거래처는 수정할 수 없는 경우
 *
 * 파트너와 연동된 거래처는 직접 수정할 수 없습니다.
 */
export type B2bCounterpartyPartnerNotUpdatableError = {
	type: "B2B_COUNTERPARTY_PARTNER_NOT_UPDATABLE"
	message?: string
}
