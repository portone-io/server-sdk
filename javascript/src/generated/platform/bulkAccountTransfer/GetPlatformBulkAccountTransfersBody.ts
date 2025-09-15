import type { PageInput } from "./../../common/PageInput"
import type { PlatformBulkAccountTransferFilterInput } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferFilterInput"
export type GetPlatformBulkAccountTransfersBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformBulkAccountTransferFilterInput
}
