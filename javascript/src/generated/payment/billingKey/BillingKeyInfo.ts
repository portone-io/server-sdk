import type { DeletedBillingKeyInfo } from "./../../payment/billingKey/DeletedBillingKeyInfo"
import type { IssuedBillingKeyInfo } from "./../../payment/billingKey/IssuedBillingKeyInfo"

/** 빌링키 정보 */
export type BillingKeyInfo =
	/** 발급 삭제 완료 */
	| DeletedBillingKeyInfo
	/** 발급 완료 */
	| IssuedBillingKeyInfo
