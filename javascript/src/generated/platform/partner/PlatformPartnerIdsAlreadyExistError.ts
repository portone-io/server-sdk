export type PlatformPartnerIdsAlreadyExistError = {
	type: "PLATFORM_PARTNER_IDS_ALREADY_EXISTS"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
