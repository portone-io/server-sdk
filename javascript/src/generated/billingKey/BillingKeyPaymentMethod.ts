import type { BillingKeyPaymentMethodCard } from "#generated/billingKey/BillingKeyPaymentMethodCard"
import type { BillingKeyPaymentMethodEasyPay } from "#generated/billingKey/BillingKeyPaymentMethodEasyPay"
import type { BillingKeyPaymentMethodMobile } from "#generated/billingKey/BillingKeyPaymentMethodMobile"
import type { BillingKeyPaymentMethodPaypal } from "#generated/billingKey/BillingKeyPaymentMethodPaypal"
import type { BillingKeyPaymentMethodTransfer } from "#generated/billingKey/BillingKeyPaymentMethodTransfer"

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
