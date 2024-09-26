/** 플랫폼 내 발생하는 여러 수수료 및 할인 분담에 관한 계산식 정보 */
export type PlatformSettlementFormula = {
	/** 플랫폼 수수료 계산식 */
	platformFee: string
	/** 할인 분담액 계산식 */
	discountShare: string
	/** 추가 수수료 계산식 */
	additionalFee: string
}
