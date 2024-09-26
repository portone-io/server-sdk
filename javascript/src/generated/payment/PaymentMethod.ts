import type { PaymentMethodCard } from "#generated/payment/PaymentMethodCard"
import type { PaymentMethodEasyPay } from "#generated/payment/PaymentMethodEasyPay"
import type { PaymentMethodGiftCertificate } from "#generated/payment/PaymentMethodGiftCertificate"
import type { PaymentMethodMobile } from "#generated/payment/PaymentMethodMobile"
import type { PaymentMethodTransfer } from "#generated/payment/PaymentMethodTransfer"
import type { PaymentMethodVirtualAccount } from "#generated/payment/PaymentMethodVirtualAccount"

/** 결제수단 정보 */
export type PaymentMethod =
	/** 결제수단 카드 정보 */
	| PaymentMethodCard
	/** 간편 결제 상세 정보 */
	| PaymentMethodEasyPay
	/** 상품권 상세 정보 */
	| PaymentMethodGiftCertificate
	/** 모바일 상세 정보 */
	| PaymentMethodMobile
	/** 계좌 이체 상세 정보 */
	| PaymentMethodTransfer
	/** 가상계좌 상세 정보 */
	| PaymentMethodVirtualAccount
