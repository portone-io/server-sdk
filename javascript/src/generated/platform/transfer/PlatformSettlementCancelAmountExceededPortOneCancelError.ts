import type { PlatformPortOnePaymentCancelAmountType } from "#generated/platform/transfer/PlatformPortOnePaymentCancelAmountType"

/** 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우 */
export type PlatformSettlementCancelAmountExceededPortOneCancelError = {
	type: "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL"
	/** (int64) */
	registeredSettlementCancelAmount: number
	/** (int64) */
	requestSettlementCancelAmount: number
	/** (int64) */
	portOneCancelAmount: number
	amountType: PlatformPortOnePaymentCancelAmountType
	message?: string
}
