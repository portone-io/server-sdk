import type { PlatformPartnerFilterInput } from "./../platform/PlatformPartnerFilterInput"
import type { SchedulePlatformPartnersBodyUpdate } from "./../platform/SchedulePlatformPartnersBodyUpdate"

export type SchedulePlatformPartnersBody = {
	filter?: PlatformPartnerFilterInput
	update: SchedulePlatformPartnersBodyUpdate
	/** (RFC 3339 date-time) */
	appliedAt: string
}
