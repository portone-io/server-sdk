import type { Bank } from "#generated/common/Bank"
import type { InstantPaymentMethodInputVirtualAccountCashReceiptInfo } from "#generated/payment/InstantPaymentMethodInputVirtualAccountCashReceiptInfo"
import type { InstantPaymentMethodInputVirtualAccountExpiry } from "#generated/payment/InstantPaymentMethodInputVirtualAccountExpiry"
import type { InstantPaymentMethodInputVirtualAccountOption } from "#generated/payment/InstantPaymentMethodInputVirtualAccountOption"

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
