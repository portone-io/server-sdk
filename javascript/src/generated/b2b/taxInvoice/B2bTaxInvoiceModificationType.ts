/** 수정 사유 */
export type B2bTaxInvoiceModificationType =
	/** 기재사항 착오 정정 */
	| "CORRECTION_OF_ENTRY_ERRORS"
	/** 공금가액 변동 */
	| "CHANGE_IN_SUPPLY_COST"
	/** 환입 */
	| "RETURN"
	/** 계약 해제 */
	| "CANCELLATION_OF_CONTRACT"
	/** 착오에 의한 이중 발급 */
	| "DUPLICATE_ISSUANCE_DUE_TO_ERROR"
	| string & {}
