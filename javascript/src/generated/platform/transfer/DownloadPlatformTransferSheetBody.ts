import type { PlatformTransferFilterInput } from "#generated/platform/transfer/PlatformTransferFilterInput"
import type { PlatformTransferSheetField } from "#generated/platform/transfer/PlatformTransferSheetField"

export type DownloadPlatformTransferSheetBody = {
	filter?: PlatformTransferFilterInput
	/** 다운로드 할 시트 컬럼 */
	fields?: PlatformTransferSheetField[]
	transferUserDefinedPropertyKeys?: string[]
	partnerUserDefinedPropertyKeys?: string[]
}
