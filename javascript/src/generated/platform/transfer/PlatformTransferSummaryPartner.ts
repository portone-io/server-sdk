import type { PlatformPartnerTaxationType } from "./../../platform/PlatformPartnerTaxationType"
import type { PlatformTransferSummaryPartnerType } from "./../../platform/transfer/PlatformTransferSummaryPartnerType"

export type PlatformTransferSummaryPartner = {
	id: string
	graphqlId: string
	name: string
	type: PlatformTransferSummaryPartnerType
	taxationType?: PlatformPartnerTaxationType
}
