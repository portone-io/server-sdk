import type { PlatformPaymentMethodCardInput } from "#generated/platform/transfer/PlatformPaymentMethodCardInput"
import type { PlatformPaymentMethodEasyPayInput } from "#generated/platform/transfer/PlatformPaymentMethodEasyPayInput"
import type { PlatformPaymentMethodGiftCertificateInput } from "#generated/platform/transfer/PlatformPaymentMethodGiftCertificateInput"
import type { PlatformPaymentMethodMobileInput } from "#generated/platform/transfer/PlatformPaymentMethodMobileInput"
import type { PlatformPaymentMethodTransferInput } from "#generated/platform/transfer/PlatformPaymentMethodTransferInput"
import type { PlatformPaymentMethodVirtualAccountInput } from "#generated/platform/transfer/PlatformPaymentMethodVirtualAccountInput"

/** 결제 수단 입력 정보 */
export type PlatformPaymentMethodInput = {
	/** 카드 */
	card?: PlatformPaymentMethodCardInput
	/** 계좌이체 */
	transfer?: PlatformPaymentMethodTransferInput
	/** 가상계좌 */
	virtualAccount?: PlatformPaymentMethodVirtualAccountInput
	/** 상품권 */
	giftCertificate?: PlatformPaymentMethodGiftCertificateInput
	/** 모바일 */
	mobile?: PlatformPaymentMethodMobileInput
	/** 간편 결제 */
	easyPay?: PlatformPaymentMethodEasyPayInput
}
