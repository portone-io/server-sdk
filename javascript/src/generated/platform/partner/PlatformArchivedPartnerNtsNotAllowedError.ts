/** 보관된 파트너는 국세청 연동/연동해제를 할 수 없는 경우 */
export type PlatformArchivedPartnerNtsNotAllowedError = {
	type: "PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED"
	message?: string
}
