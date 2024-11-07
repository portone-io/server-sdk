import type { PlatformFeeInput } from "./../platform/PlatformFeeInput"
import type { PlatformPayer } from "./../platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "./../platform/PlatformSettlementCycleInput"

/**
 * 계약 업데이트를 위한 입력 정보. 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 *
 * 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 */
export type UpdatePlatformContractBody = {
	/** 계약 이름 */
	name?: string
	/** 계약 내부 표기를 위한 메모 */
	memo?: string
	/** 중개수수료 */
	platformFee?: PlatformFeeInput
	/** 정산 주기 */
	settlementCycle?: PlatformSettlementCycleInput
	/** 중개수수료에 대한 부가세 부담 주체 */
	platformFeeVatPayer?: PlatformPayer
	/** 정산 시 결제금액 부가세 감액 여부 */
	subtractPaymentVatAmount?: boolean
}
