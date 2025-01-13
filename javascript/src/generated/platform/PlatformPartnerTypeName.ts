/** 플랫폼 파트너 유형 이름 */
export type PlatformPartnerTypeName =
	/** 사업자 */
	| "BUSINESS"
	/** 원천징수 대상자 */
	| "WHT_PAYER"
	/** 원천징수 비대상자 */
	| "NON_WHT_PAYER"
	| string & {}
