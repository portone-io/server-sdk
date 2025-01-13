/** 플랫폼 과세 유형 */
export type PlatformTaxationType =
	/** 일반 과세 */
	| "NORMAL"
	/** 간이과세(세금계산서 발행) */
	| "SIMPLE_TAX_INVOICE_ISSUER"
	/** 간이과세(세금계산서 미발행) */
	| "SIMPLE"
	/** 면세 */
	| "TAX_FREE"
	/** 고유 번호 부여 사업자 (비영리, 국가 등 납세 의무가 없는) */
	| "ASSIGNED_ID_NUMBER"
	/** 과세 특례자 */
	| "SPECIAL"
	| string & {}
