import type { PageInput } from "./../../common/PageInput"
import type { PlatformAccountTransferFilter } from "./../../platform/accountTransfer/PlatformAccountTransferFilter"
export type GetAccountTransfersBody1 = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformAccountTransferFilter
}
