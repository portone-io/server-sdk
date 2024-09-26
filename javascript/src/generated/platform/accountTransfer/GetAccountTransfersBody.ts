import type { PageInput } from "#generated/common/PageInput"
import type { PlatformAccountTransferFilter } from "#generated/platform/accountTransfer/PlatformAccountTransferFilter"

export type GetAccountTransfersBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformAccountTransferFilter
}
