/** 파트너의 국세청 연동/해제가 진행 중인 경우 */
export type PlatformPartnerPendingNtsOperationError = {
	type: "PLATFORM_PARTNER_PENDING_NTS_OPERATION"
	message?: string
}
