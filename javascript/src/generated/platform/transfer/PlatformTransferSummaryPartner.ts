import type { PlatformPartnerTaxationType } from "#generated/platform/PlatformPartnerTaxationType"
import type { PlatformTransferSummaryPartnerType } from "#generated/platform/transfer/PlatformTransferSummaryPartnerType"

export type PlatformTransferSummaryPartner = {
	id: string
	graphqlId: string
	name: string
	type: PlatformTransferSummaryPartnerType
	taxationType?: PlatformPartnerTaxationType
}
