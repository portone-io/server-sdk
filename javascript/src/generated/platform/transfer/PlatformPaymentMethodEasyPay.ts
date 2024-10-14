import type { EasyPayMethodType } from "#generated/platform/transfer/EasyPayMethodType"
import type { EasyPayProvider } from "#generated/common/EasyPayProvider"

/** 간편 결제 */
export type PlatformPaymentMethodEasyPay = {
	type: "EASY_PAY"
	/** 간편 결제사 */
	provider?: EasyPayProvider
	/** 간편 결제 수단 */
	methodType?: EasyPayMethodType
}