import type { BillingKeyPaymentMethodCard } from "#generated/payment/billingKey/BillingKeyPaymentMethodCard"
import type { BillingKeyPaymentMethodEasyPay } from "#generated/payment/billingKey/BillingKeyPaymentMethodEasyPay"
import type { BillingKeyPaymentMethodMobile } from "#generated/payment/billingKey/BillingKeyPaymentMethodMobile"
import type { BillingKeyPaymentMethodPaypal } from "#generated/payment/billingKey/BillingKeyPaymentMethodPaypal"
import type { BillingKeyPaymentMethodTransfer } from "#generated/payment/billingKey/BillingKeyPaymentMethodTransfer"

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
