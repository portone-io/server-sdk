import type { Bank } from "./../../common/Bank"
export type PlatformPayoutAccount = {
	bank: Bank
	number: string
	holder: string
}
