export type PlatformAdditionalFeePoliciesNotFoundError = {
	type: "PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND"
	ids: string[]
	graphqlIds: string[]
	message?: string
}
