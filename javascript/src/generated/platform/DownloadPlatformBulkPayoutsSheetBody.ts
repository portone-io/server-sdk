import type { PlatformBulkPayoutFilterInput } from "#generated/platform/bulkPayout/PlatformBulkPayoutFilterInput"
import type { PlatformBulkPayoutsSheetField } from "#generated/platform/PlatformBulkPayoutsSheetField"

export type DownloadPlatformBulkPayoutsSheetBody = {
	filter?: PlatformBulkPayoutFilterInput
	/** 다운로드 할 시트 컬럼 */
	fields?: PlatformBulkPayoutsSheetField[]
	isForTest?: boolean
}
