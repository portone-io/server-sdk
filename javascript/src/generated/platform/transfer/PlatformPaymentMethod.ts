import type { PlatformPaymentMethodCard } from "#generated/platform/transfer/PlatformPaymentMethodCard"
import type { PlatformPaymentMethodEasyPay } from "#generated/platform/transfer/PlatformPaymentMethodEasyPay"
import type { PlatformPaymentMethodGiftCertificate } from "#generated/platform/transfer/PlatformPaymentMethodGiftCertificate"
import type { PlatformPaymentMethodMobile } from "#generated/platform/transfer/PlatformPaymentMethodMobile"
import type { PlatformPaymentMethodTransfer } from "#generated/platform/transfer/PlatformPaymentMethodTransfer"
import type { PlatformPaymentMethodVirtualAccount } from "#generated/platform/transfer/PlatformPaymentMethodVirtualAccount"

/** 결제 수단 */
export type PlatformPaymentMethod =
	/** 카드 */
	| PlatformPaymentMethodCard
	/** 간편 결제 */
	| PlatformPaymentMethodEasyPay
	/** 상품권 */
	| PlatformPaymentMethodGiftCertificate
	/** 모바일 */
	| PlatformPaymentMethodMobile
	/** 계좌이체 */
	| PlatformPaymentMethodTransfer
	/** 가상계좌 */
	| PlatformPaymentMethodVirtualAccount
