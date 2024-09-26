export type PlatformPartnerIdsDuplicatedError = {
	type: "PLATFORM_PARTNER_IDS_DUPLICATED"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
