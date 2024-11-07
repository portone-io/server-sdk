import type { PlatformFixedAmountFee } from "./../platform/PlatformFixedAmountFee"
import type { PlatformFixedRateFee } from "./../platform/PlatformFixedRateFee"

/** 플랫폼 중개수수료 정보 */
export type PlatformFee =
	/** 정액 수수료 */
	| PlatformFixedAmountFee
	/** 정률 수수료 */
	| PlatformFixedRateFee
