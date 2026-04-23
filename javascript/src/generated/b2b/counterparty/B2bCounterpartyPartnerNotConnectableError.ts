/**
 * 파트너 연동 거래처는 국세청 연동이 허용되지 않는 경우
 *
 * 파트너와 연동된 거래처는 국세청 연동을 직접 수행할 수 없습니다.
 */
export type B2bCounterpartyPartnerNotConnectableError = {
	type: "B2B_COUNTERPARTY_PARTNER_NOT_CONNECTABLE"
	message?: string
}
