import type { PlatformRoundType } from "#generated/platform/PlatformRoundType"
import type { PlatformSettlementFormula } from "#generated/platform/PlatformSettlementFormula"
import type { PlatformSettlementRule } from "#generated/platform/PlatformSettlementRule"

/** 고객사의 플랫폼 기능 관련 정보 */
export type Platform = {
	/** 해당 플랫폼의 고객사 아이디 */
	merchantId: string
	graphqlId: string
	/** 파트너 정산금액의 소수점 처리 방식 */
	roundType: PlatformRoundType
	/** 수수료 및 할인 분담 정책 관련 계산식 */
	settlementFormula: PlatformSettlementFormula
	/** 정산 규칙 */
	settlementRule: PlatformSettlementRule
}
