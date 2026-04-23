/** 삭제할 수 없는 정산건이 포함된 경우 */
export type PlatformNonDeletablePartnerSettlementsError = {
	type: "PLATFORM_NON_DELETABLE_PARTNER_SETTLEMENTS"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
