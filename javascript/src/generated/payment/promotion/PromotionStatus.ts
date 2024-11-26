export type PromotionStatus =
	/** 예정됨 */
	| "SCHEDULED"
	/** 진행중 */
	| "IN_PROGRESS"
	/** 일시 중지됨 */
	| "PAUSED"
	/** 예산 소진됨 */
	| "BUDGET_EXHAUSTED"
	/** 중단됨 */
	| "TERMINATED"
	/** 완료됨 */
	| "COMPLETED"
	| string & {}
