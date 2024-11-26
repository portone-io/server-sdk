import type { PlatformAdditionalFeePolicy } from "./../../platform/PlatformAdditionalFeePolicy"
/** 추가 수수료 정보 */
export type PlatformOrderTransferAdditionalFee = {
	/** 추가 수수료 정책 */
	policy: PlatformAdditionalFeePolicy
	/**
	 * 추가 수수료 금액
	 * (int64)
	 */
	amount: number
	/**
	 * 추가 수수료 부가세 금액
	 * (int64)
	 */
	vat: number
}
