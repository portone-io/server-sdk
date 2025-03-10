import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformPaymentMethodCard } from "./../../platform/transfer/PlatformPaymentMethodCard"
import type { PlatformPaymentMethodEasyPay } from "./../../platform/transfer/PlatformPaymentMethodEasyPay"
import type { PlatformPaymentMethodGiftCertificate } from "./../../platform/transfer/PlatformPaymentMethodGiftCertificate"
import type { PlatformPaymentMethodMobile } from "./../../platform/transfer/PlatformPaymentMethodMobile"
import type { PlatformPaymentMethodTransfer } from "./../../platform/transfer/PlatformPaymentMethodTransfer"
import type { PlatformPaymentMethodVirtualAccount } from "./../../platform/transfer/PlatformPaymentMethodVirtualAccount"
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
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformPaymentMethod(entity: PlatformPaymentMethod): entity is { readonly type: Unrecognized } {
	return entity.type !== "CARD"
		&& entity.type !== "EASY_PAY"
		&& entity.type !== "GIFT_CERTIFICATE"
		&& entity.type !== "MOBILE"
		&& entity.type !== "TRANSFER"
		&& entity.type !== "VIRTUAL_ACCOUNT"
}
