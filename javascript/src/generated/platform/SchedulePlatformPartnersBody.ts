import type { PlatformPartnerFilterInput } from "#generated/platform/PlatformPartnerFilterInput"
import type { SchedulePlatformPartnersBodyUpdate } from "#generated/platform/SchedulePlatformPartnersBodyUpdate"

export type SchedulePlatformPartnersBody = {
	filter?: PlatformPartnerFilterInput
	update: SchedulePlatformPartnersBodyUpdate
	/** (RFC 3339 date-time) */
	appliedAt: string
}
