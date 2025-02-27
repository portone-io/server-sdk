export type PlatformBulkTaskStatus =
	| "PREPARED"
	| "PROCESSING"
	| "COMPLETED"
	| "CANCELED"
	| string & {}
