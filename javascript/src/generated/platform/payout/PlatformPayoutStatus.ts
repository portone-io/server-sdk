export type PlatformPayoutStatus =
	| "CONFIRMED"
	| "PREPARED"
	| "CANCELLED"
	| "STOPPED"
	| "PROCESSING"
	| "SUCCEEDED"
	| "FAILED"
	| "SCHEDULED"
	| string & {}
