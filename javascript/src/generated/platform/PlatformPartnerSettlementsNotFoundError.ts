/** 요청한 정산건 목록을 찾을 수 없는 경우 */
export type PlatformPartnerSettlementsNotFoundError = {
	type: "PLATFORM_PARTNER_SETTLEMENTS_NOT_FOUND"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
