import type { PlatformDiscountSharePolicy } from "#generated/platform/PlatformDiscountSharePolicy"

/** 할인 정보 */
export type PlatformOrderTransferDiscount = {
	/** 할인 분담 정책 */
	sharePolicy: PlatformDiscountSharePolicy
	/**
	 * 할인 금액
	 * (int64)
	 */
	amount: number
	/**
	 * 면세 할인 금액
	 * (int64)
	 */
	taxFreeAmount: number
	/**
	 * 할인 분담 금액
	 * (int64)
	 */
	shareAmount: number
	/**
	 * 면세 할인 분담 금액
	 * (int64)
	 */
	shareTaxFreeAmount: number
}
