import type { PlatformPaymentChannel } from "#generated/platform/PlatformPaymentChannel"

export type PlatformTransferFilterOptions = {
	partnerTags: string[]
	contractIds: string[]
	additionalFeePolicyIds: string[]
	discountSharePolicyIds: string[]
	/** 채널 */
	paymentChannels: PlatformPaymentChannel[]
}
