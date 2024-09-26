import type { PlatformProperties } from "#generated/platform/PlatformProperties"
import type { SchedulePlatformPartnersBodyUpdateAccount } from "#generated/platform/SchedulePlatformPartnersBodyUpdateAccount"
import type { SchedulePlatformPartnersBodyUpdateContact } from "#generated/platform/SchedulePlatformPartnersBodyUpdateContact"
import type { SchedulePlatformPartnersBodyUpdateType } from "#generated/platform/SchedulePlatformPartnersBodyUpdateType"

export type SchedulePlatformPartnersBodyUpdate = {
	name?: string
	contact?: SchedulePlatformPartnersBodyUpdateContact
	type?: SchedulePlatformPartnersBodyUpdateType
	account?: SchedulePlatformPartnersBodyUpdateAccount
	defaultContractId?: string
	memo?: string
	tags?: string[]
	userDefinedProperties?: PlatformProperties
}
