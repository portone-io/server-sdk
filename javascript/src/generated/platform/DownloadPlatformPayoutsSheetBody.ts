import type { PlatformPayoutFilterInput } from "#generated/platform/payout/PlatformPayoutFilterInput"
import type { PlatformPayoutsSheetField } from "#generated/platform/PlatformPayoutsSheetField"

export type DownloadPlatformPayoutsSheetBody = {
	filter?: PlatformPayoutFilterInput
	/** 다운로드 할 시트 컬럼 */
	fields?: PlatformPayoutsSheetField[]
	isForTest?: boolean
}
