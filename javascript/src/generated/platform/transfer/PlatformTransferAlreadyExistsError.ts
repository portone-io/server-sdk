export type PlatformTransferAlreadyExistsError = {
	type: "PLATFORM_TRANSFER_ALREADY_EXISTS"
	transferId: string
	transferGraphqlId: string
	message?: string
}
