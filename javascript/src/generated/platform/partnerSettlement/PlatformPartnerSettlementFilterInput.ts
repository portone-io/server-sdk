import type { Currency } from "./../../common/Currency"
import type { PlatformPartnerSettlementFilterKeywordInput } from "./../../platform/partnerSettlement/PlatformPartnerSettlementFilterKeywordInput"
import type { PlatformPartnerSettlementStatus } from "./../../platform/partnerSettlement/PlatformPartnerSettlementStatus"
import type { PlatformPartnerSettlementType } from "./../../platform/partnerSettlement/PlatformPartnerSettlementType"

export type PlatformPartnerSettlementFilterInput = {
	settlementDates?: string[]
	contractIds?: string[]
	partnerTags?: string[]
	/** 통화 단위 */
	settlementCurrencies?: Currency[]
	/** 정산 상태 */
	statuses?: PlatformPartnerSettlementStatus[]
	partnerIds?: string[]
	/** 정산 유형 */
	settlementTypes?: PlatformPartnerSettlementType[]
	keyword?: PlatformPartnerSettlementFilterKeywordInput
}
