import type { InstantBillingKeyPaymentMethodInputCard } from "./../../payment/billingKey/InstantBillingKeyPaymentMethodInputCard"
/**
 * 빌링키 발급 시 결제 수단 입력 양식
 *
 * `card`를 반드시 입력해 주세요.
 */
export type InstantBillingKeyPaymentMethodInput = {
	card?: InstantBillingKeyPaymentMethodInputCard
}
