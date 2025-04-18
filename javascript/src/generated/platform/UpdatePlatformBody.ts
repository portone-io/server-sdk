import type { UpdatePlatformBodySettlementRule } from "./../platform/UpdatePlatformBodySettlementRule"
/**
 * 플랫폼 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
export type UpdatePlatformBody = {
	/** 정산 규칙 */
	settlementRule?: UpdatePlatformBodySettlementRule
}
