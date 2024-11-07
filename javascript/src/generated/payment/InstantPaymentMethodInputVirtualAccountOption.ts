import type { InstantPaymentMethodInputVirtualAccountOptionFixed } from "./../payment/InstantPaymentMethodInputVirtualAccountOptionFixed"
import type { InstantPaymentMethodInputVirtualAccountOptionType } from "./../payment/InstantPaymentMethodInputVirtualAccountOptionType"

/** 가상계좌 발급 방식 */
export type InstantPaymentMethodInputVirtualAccountOption = {
	/** 발급 유형 */
	type: InstantPaymentMethodInputVirtualAccountOptionType
	/**
	 * 고정식 가상계좌 발급 방식
	 *
	 * 발급 유형을 FIXED 로 선택했을 시에만 입력합니다.
	 */
	fixed?: InstantPaymentMethodInputVirtualAccountOptionFixed
}
