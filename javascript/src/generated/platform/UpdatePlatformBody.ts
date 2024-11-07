import type { PlatformRoundType } from "./../platform/PlatformRoundType"
import type { UpdatePlatformBodySettlementFormula } from "./../platform/UpdatePlatformBodySettlementFormula"
import type { UpdatePlatformBodySettlementRule } from "./../platform/UpdatePlatformBodySettlementRule"

/**
 * 플랫폼 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
export type UpdatePlatformBody = {
	/** 파트너 정산금액의 소수점 처리 방식 */
	roundType?: PlatformRoundType
	/** 수수료 및 할인 분담 정책 관련 계산식 */
	settlementFormula?: UpdatePlatformBodySettlementFormula
	/** 정산 규칙 */
	settlementRule?: UpdatePlatformBodySettlementRule
}
