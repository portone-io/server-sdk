import type { InstantPaymentMethodInputCard } from "./../payment/InstantPaymentMethodInputCard"
import type { InstantPaymentMethodInputVirtualAccount } from "./../payment/InstantPaymentMethodInputVirtualAccount"

/**
 * 수기 결제 수단 입력 정보
 *
 * 하나의 필드만 입력합니다.
 */
export type InstantPaymentMethodInput = {
	/** 카드 */
	card?: InstantPaymentMethodInputCard
	/** 가상계좌 */
	virtualAccount?: InstantPaymentMethodInputVirtualAccount
}
