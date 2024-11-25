import type { PlatformFee } from "./../platform/PlatformFee"
import type { PlatformPayer } from "./../platform/PlatformPayer"
import type { PlatformSettlementCycle } from "./../platform/PlatformSettlementCycle"
/**
 * 계약
 *
 * 계약은 플랫폼 고객사가 파트너에게 정산해줄 대금과 정산일을 계산하는 데 적용되는 정보입니다.
 * 고객사의 플랫폼에서 재화 및 서비스를 판매하기 위한 중개수수료와 판매금에 대한 정산일로 구성되어 있습니다.
 */
export type PlatformContract = {
	/** 계약 고유 아이디 */
	id: string
	graphqlId: string
	/** 계약 이름 */
	name: string
	/** 계약 내부 표기를 위한 메모 */
	memo?: string
	/** 중개수수료 */
	platformFee: PlatformFee
	/** 정산 주기 */
	settlementCycle: PlatformSettlementCycle
	/** 중개수수료에 대한 부가세 부담 주체 */
	platformFeeVatPayer: PlatformPayer
	/**
	 * 정산 시 결제금액 부가세 감액 여부
	 *
	 * false인 경우 정산금에서 결제 금액 부가세를 감액하지 않고, true인 경우 정산금에서 결제 금액 부가세를 감액합니다.
	 */
	subtractPaymentVatAmount: boolean
	/** 보관 여부 */
	isArchived: boolean
	/**
	 * 변경 적용 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
