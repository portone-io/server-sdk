import type { Currency } from "#generated/common/Currency"
import type { PlatformContract } from "#generated/platform/PlatformContract"
import type { PlatformOrderSettlementAmount } from "#generated/platform/PlatformOrderSettlementAmount"
import type { PlatformOrderTransferAdditionalFee } from "#generated/platform/transfer/PlatformOrderTransferAdditionalFee"
import type { PlatformOrderTransferCancellation } from "#generated/platform/transfer/PlatformOrderTransferCancellation"
import type { PlatformOrderTransferDiscount } from "#generated/platform/transfer/PlatformOrderTransferDiscount"
import type { PlatformOrderTransferOrderLine } from "#generated/platform/transfer/PlatformOrderTransferOrderLine"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"
import type { PlatformPayment } from "#generated/platform/transfer/PlatformPayment"
import type { PlatformTransferStatus } from "#generated/platform/transfer/PlatformTransferStatus"
import type { PlatformUserDefinedPropertyKeyValue } from "#generated/platform/transfer/PlatformUserDefinedPropertyKeyValue"
import type { TransferParameters } from "#generated/platform/transfer/TransferParameters"

/** 주문 취소 정산건 */
export type PlatformOrderCancelTransfer = {
	type: "ORDER_CANCEL"
	/** 정산건 아이디 */
	id: string
	graphqlId: string
	/** 파트너 */
	partner: PlatformPartner
	/** 정산 상태 */
	status: PlatformTransferStatus
	/** 메모 */
	memo?: string
	/**
	 * 정산 일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	settlementDate: string
	/** 정산 통화 */
	settlementCurrency: Currency
	payoutId?: string
	payoutGraphqlId?: string
	/** 테스트 모드 여부 */
	isForTest: boolean
	/** 사용자 정의 속성 */
	userDefinedProperties: PlatformUserDefinedPropertyKeyValue[]
	/** 정산 금액 정보 */
	amount: PlatformOrderSettlementAmount
	/** 계약 */
	contract: PlatformContract
	/** 결제 정보 */
	payment: PlatformPayment
	/**
	 * 정산 시작일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	settlementStartDate: string
	/** 주문 항목 리스트 */
	orderLines: PlatformOrderTransferOrderLine[]
	/** 정산 금액 계산 시 사용된 추가 수수료 정보 */
	additionalFees: PlatformOrderTransferAdditionalFee[]
	/** 정산 금액 계산 시 사용된 할인 정보 */
	discounts: PlatformOrderTransferDiscount[]
	/** 주문 취소 정보 */
	cancellation: PlatformOrderTransferCancellation
	/** 정산 파라미터 (실험기능) */
	parameters: TransferParameters
}
