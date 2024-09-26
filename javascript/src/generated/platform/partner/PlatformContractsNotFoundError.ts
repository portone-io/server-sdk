export type PlatformContractsNotFoundError = {
	type: "PLATFORM_CONTRACTS_NOT_FOUND"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
