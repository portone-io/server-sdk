import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformTransferSummary } from "./../../platform/transfer/PlatformTransferSummary"

export type GetPlatformTransferSummariesResponse = {
	transferSummaries: PlatformTransferSummary[]
	page: PageInfo
}
