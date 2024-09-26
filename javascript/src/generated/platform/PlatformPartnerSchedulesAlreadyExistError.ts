export type PlatformPartnerSchedulesAlreadyExistError = {
	type: "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
