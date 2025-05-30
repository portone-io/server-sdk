export type SettlementAmountType =
	/** 순액(공급가액) */
	| "NET"
	/** 총액(공급가액, 부가세) */
	| "GROSS"
	| string & {}
