import type { Bank } from "#generated/common/Bank"

export type PlatformPayoutAccount = {
	bank: Bank
	number: string
	holder: string
}
