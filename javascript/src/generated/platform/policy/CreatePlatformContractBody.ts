import type { PlatformFeeInput } from "#generated/platform/PlatformFeeInput"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "#generated/platform/PlatformSettlementCycleInput"

/** 계약 객체 생성을 위한 입력 정보 */
export type CreatePlatformContractBody = {
	/**
	 * 계약에 부여할 고유 아이디
	 *
	 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
	 */
	id?: string
	/** 계약 이름 */
	name: string
	/** 계약 내부 표기를 위한 메모 */
	memo?: string
	/** 중개수수료 */
	platformFee: PlatformFeeInput
	/** 정산 주기 */
	settlementCycle: PlatformSettlementCycleInput
	/** 중개수수료에 대한 부가세 부담 주체 */
	platformFeeVatPayer: PlatformPayer
	/** 정산 시 결제금액 부가세 감액 여부 */
	subtractPaymentVatAmount: boolean
}
