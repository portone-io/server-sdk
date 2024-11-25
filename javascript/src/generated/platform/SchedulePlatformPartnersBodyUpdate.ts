import type { PlatformProperties } from "./../platform/PlatformProperties"
import type { SchedulePlatformPartnersBodyUpdateAccount } from "./../platform/SchedulePlatformPartnersBodyUpdateAccount"
import type { SchedulePlatformPartnersBodyUpdateContact } from "./../platform/SchedulePlatformPartnersBodyUpdateContact"
import type { SchedulePlatformPartnersBodyUpdateType } from "./../platform/SchedulePlatformPartnersBodyUpdateType"
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
