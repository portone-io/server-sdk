import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformBulkAccountTransfer } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransfer"
import type { PlatformBulkAccountTransferStatusStats } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferStatusStats"
export type GetPlatformBulkAccountTransfersResponse = {
	items: PlatformBulkAccountTransfer[]
	page: PageInfo
	counts: PlatformBulkAccountTransferStatusStats
}
