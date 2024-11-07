import type { Bank } from "./../common/Bank"
import type { InstantPaymentMethodInputVirtualAccountCashReceiptInfo } from "./../payment/InstantPaymentMethodInputVirtualAccountCashReceiptInfo"
import type { InstantPaymentMethodInputVirtualAccountExpiry } from "./../payment/InstantPaymentMethodInputVirtualAccountExpiry"
import type { InstantPaymentMethodInputVirtualAccountOption } from "./../payment/InstantPaymentMethodInputVirtualAccountOption"

/** 가상계좌 수단 정보 입력 정보 */
export type InstantPaymentMethodInputVirtualAccount = {
	/** 은행 */
	bank: Bank
	/** 입금 만료 기한 */
	expiry: InstantPaymentMethodInputVirtualAccountExpiry
	/** 가상계좌 유형 */
	option: InstantPaymentMethodInputVirtualAccountOption
	/** 현금영수증 정보 */
	cashReceipt: InstantPaymentMethodInputVirtualAccountCashReceiptInfo
	/** 예금주명 */
	remitteeName?: string
}
