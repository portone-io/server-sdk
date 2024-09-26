/**
 * 플랫폼 업데이트 시 변경할 계산식 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
export type UpdatePlatformBodySettlementFormula = {
	/** 플랫폼 수수료 계산식 */
	platformFee?: string
	/** 할인 분담액 계산식 */
	discountShare?: string
	/** 추가 수수료 계산식 */
	additionalFee?: string
}
