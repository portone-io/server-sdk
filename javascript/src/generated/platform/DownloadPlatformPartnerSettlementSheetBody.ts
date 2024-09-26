import type { PlatformPartnerSettlementFilterInput } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementFilterInput"
import type { PlatformPartnerSettlementSheetField } from "#generated/platform/PlatformPartnerSettlementSheetField"

export type DownloadPlatformPartnerSettlementSheetBody = {
	filter?: PlatformPartnerSettlementFilterInput
	/** 다운로드 할 시트 컬럼 */
	fields?: PlatformPartnerSettlementSheetField[]
	isForTest?: boolean
}
