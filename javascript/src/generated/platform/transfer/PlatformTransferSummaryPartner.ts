import type { PlatformPartnerTaxationType } from "./../../platform/PlatformPartnerTaxationType"
import type { PlatformTransferSummaryPartnerType } from "./../../platform/transfer/PlatformTransferSummaryPartnerType"
import type { PlatformUserDefinedPropertyKeyValue } from "./../../platform/transfer/PlatformUserDefinedPropertyKeyValue"
export type PlatformTransferSummaryPartner = {
	id: string
	graphqlId: string
	name: string
	type: PlatformTransferSummaryPartnerType
	taxationType?: PlatformPartnerTaxationType
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
}
