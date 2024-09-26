import type { ReconciliationPaymentMethodArs } from "#generated/platform/ReconciliationPaymentMethodArs"
import type { ReconciliationPaymentMethodCard } from "#generated/platform/ReconciliationPaymentMethodCard"
import type { ReconciliationPaymentMethodCharge } from "#generated/platform/ReconciliationPaymentMethodCharge"
import type { ReconciliationPaymentMethodEasyPay } from "#generated/platform/ReconciliationPaymentMethodEasyPay"
import type { ReconciliationPaymentMethodEtc } from "#generated/platform/ReconciliationPaymentMethodEtc"
import type { ReconciliationPaymentMethodGiftCertificate } from "#generated/platform/ReconciliationPaymentMethodGiftCertificate"
import type { ReconciliationPaymentMethodMobile } from "#generated/platform/ReconciliationPaymentMethodMobile"
import type { ReconciliationPaymentMethodTransfer } from "#generated/platform/ReconciliationPaymentMethodTransfer"
import type { ReconciliationPaymentMethodVirtualAccount } from "#generated/platform/ReconciliationPaymentMethodVirtualAccount"

export type ReconciliationPaymentMethod =
	/** ARS 결제 */
	| ReconciliationPaymentMethodArs
	/** 카드 결제 */
	| ReconciliationPaymentMethodCard
	/** 간편결제 충전 */
	| ReconciliationPaymentMethodCharge
	/** 간편 결제 */
	| ReconciliationPaymentMethodEasyPay
	/** 기타 결제 */
	| ReconciliationPaymentMethodEtc
	/** 상품권 결제 */
	| ReconciliationPaymentMethodGiftCertificate
	/** 모바일 결제 */
	| ReconciliationPaymentMethodMobile
	/** 계좌이체 */
	| ReconciliationPaymentMethodTransfer
	/** 가상계좌 결제 */
	| ReconciliationPaymentMethodVirtualAccount
