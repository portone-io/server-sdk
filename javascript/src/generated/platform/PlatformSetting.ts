import type { SettlementAmountType } from "./../platform/SettlementAmountType"
/** 플랫폼 설정 */
export type PlatformSetting = {
	/** 기본 보내는 이 통장 메모 */
	defaultWithdrawalMemo?: string
	/** 기본 받는 이 통장 메모 */
	defaultDepositMemo?: string
	/** paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부 */
	supportsMultipleOrderTransfersPerPartner: boolean
	/** 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부 */
	adjustSettlementDateAfterHolidayIfEarlier: boolean
	/** 지급 금액에서 원천징수세 차감 여부 */
	deductWht: boolean
	/** 정산 금액 취급 기준 */
	settlementAmountType: SettlementAmountType
}
