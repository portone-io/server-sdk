export type PlatformBulkPayoutStatus =
	| "SCHEDULED"
	| "PREPARING"
	| "PREPARED"
	| "ONGOING"
	| "CANCELLED"
	| "STOPPED"
	| "COMPLETED"
	| string & {}
