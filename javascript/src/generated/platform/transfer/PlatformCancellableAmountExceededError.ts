import type { PlatformCancellableAmountType } from "./../../platform/transfer/PlatformCancellableAmountType"

/** 취소 가능한 금액이 초과한 경우 */
export type PlatformCancellableAmountExceededError = {
	type: "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED"
	/** (int64) */
	cancellableAmount: number
	/** (int64) */
	requestAmount: number
	amountType: PlatformCancellableAmountType
	message?: string
}
