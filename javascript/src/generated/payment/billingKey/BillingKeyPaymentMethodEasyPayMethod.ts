import type { BillingKeyPaymentMethodCard } from "#generated/payment/billingKey/BillingKeyPaymentMethodCard"
import type { BillingKeyPaymentMethodEasyPayCharge } from "#generated/payment/billingKey/BillingKeyPaymentMethodEasyPayCharge"
import type { BillingKeyPaymentMethodTransfer } from "#generated/payment/billingKey/BillingKeyPaymentMethodTransfer"

/** 간편 결제 수단 */
export type BillingKeyPaymentMethodEasyPayMethod =
	/** 카드 정보 */
	| BillingKeyPaymentMethodCard
	/** 충전식 포인트 결제 정보 */
	| BillingKeyPaymentMethodEasyPayCharge
	/** 계좌이체 정보 */
	| BillingKeyPaymentMethodTransfer
