import type { PlatformBulkAccountTransferFilterInputCriteria } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferFilterInputCriteria"
import type { PlatformBulkAccountTransferStatus } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferStatus"
export type PlatformBulkAccountTransferFilterInput = {
	statuses?: PlatformBulkAccountTransferStatus[]
	criteria?: PlatformBulkAccountTransferFilterInputCriteria
}
