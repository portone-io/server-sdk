import type { PaymentMethodCard } from "./../payment/PaymentMethodCard"
import type { PaymentMethodEasyPay } from "./../payment/PaymentMethodEasyPay"
import type { PaymentMethodGiftCertificate } from "./../payment/PaymentMethodGiftCertificate"
import type { PaymentMethodMobile } from "./../payment/PaymentMethodMobile"
import type { PaymentMethodTransfer } from "./../payment/PaymentMethodTransfer"
import type { PaymentMethodVirtualAccount } from "./../payment/PaymentMethodVirtualAccount"

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
