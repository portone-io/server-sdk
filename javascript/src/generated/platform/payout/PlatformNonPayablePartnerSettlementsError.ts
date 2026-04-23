/** 지급할 수 없는 정산건이 포함된 경우 */
export type PlatformNonPayablePartnerSettlementsError = {
	type: "PLATFORM_NON_PAYABLE_PARTNER_SETTLEMENTS"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
