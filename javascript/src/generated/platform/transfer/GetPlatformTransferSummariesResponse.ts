import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformTransferSummary } from "#generated/platform/transfer/PlatformTransferSummary"

export type GetPlatformTransferSummariesResponse = {
	transferSummaries: PlatformTransferSummary[]
	page: PageInfo
}
