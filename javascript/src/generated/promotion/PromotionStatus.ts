export type PromotionStatus =
	/** 진행중 */
	| "IN_PROGRESS"
	/** 중단됨 */
	| "TERMINATED"
	/** 완료됨 */
	| "COMPLETED"
	/** 예정됨 */
	| "SCHEDULED"
	/** 일시 중지됨 */
	| "PAUSED"
	/** 예산 소진됨 */
	| "BUDGET_EXHAUSTED"
