import type { EasyPayMethodType } from "./../../platform/transfer/EasyPayMethodType"
import type { EasyPayProvider } from "./../../common/EasyPayProvider"

/** 간편 결제 입력 정보 */
export type PlatformPaymentMethodEasyPayInput = {
	/** 간편 결제사 */
	provider?: EasyPayProvider
	/** 간편 결제 수단 */
	methodType?: EasyPayMethodType
}
