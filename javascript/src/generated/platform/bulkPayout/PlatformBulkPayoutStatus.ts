export type PlatformBulkPayoutStatus =
	| "PREPARING"
	| "PREPARED"
	| "ONGOING"
	| "POST_PROCESS_PENDING"
	| "CANCELLED"
	| "COMPLETED"
	| string & {}
