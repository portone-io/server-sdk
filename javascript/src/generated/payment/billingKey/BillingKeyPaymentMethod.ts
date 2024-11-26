import type { Unrecognized } from "./../../../utils/unrecognized"
import type { BillingKeyPaymentMethodCard } from "./../../payment/billingKey/BillingKeyPaymentMethodCard"
import type { BillingKeyPaymentMethodEasyPay } from "./../../payment/billingKey/BillingKeyPaymentMethodEasyPay"
import type { BillingKeyPaymentMethodMobile } from "./../../payment/billingKey/BillingKeyPaymentMethodMobile"
import type { BillingKeyPaymentMethodPaypal } from "./../../payment/billingKey/BillingKeyPaymentMethodPaypal"
import type { BillingKeyPaymentMethodTransfer } from "./../../payment/billingKey/BillingKeyPaymentMethodTransfer"
/** 빌링키 발급 수단 정보 */
export type BillingKeyPaymentMethod =
	/** 카드 정보 */
	| BillingKeyPaymentMethodCard
	/** 간편 결제 정보 */
	| BillingKeyPaymentMethodEasyPay
	/** 모바일 정보 */
	| BillingKeyPaymentMethodMobile
	/** 페이팔 정보 */
	| BillingKeyPaymentMethodPaypal
	/** 계좌이체 정보 */
	| BillingKeyPaymentMethodTransfer
	| { readonly type: Unrecognized }

export function isUnrecognizedBillingKeyPaymentMethod(entity: BillingKeyPaymentMethod): entity is { readonly type: Unrecognized } {
	return entity.type !== "BillingKeyPaymentMethodCard"
		&& entity.type !== "BillingKeyPaymentMethodEasyPay"
		&& entity.type !== "BillingKeyPaymentMethodMobile"
		&& entity.type !== "BillingKeyPaymentMethodPaypal"
		&& entity.type !== "BillingKeyPaymentMethodTransfer"
}
