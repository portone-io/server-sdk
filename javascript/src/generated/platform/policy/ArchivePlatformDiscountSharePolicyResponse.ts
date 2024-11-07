import type { PlatformDiscountSharePolicy } from "./../../platform/PlatformDiscountSharePolicy"

/** 할인 분담 보관 성공 응답 */
export type ArchivePlatformDiscountSharePolicyResponse = {
	/** 보관된 할인 분담 */
	discountSharePolicy: PlatformDiscountSharePolicy
}
