export type PlatformAccountTransferStatusStats = {
	/** (int64) */
	prepared: number
	/** (int64) */
	scheduled: number
	/** (int64) */
	cancelled: number
	/** (int64) */
	stopped: number
	/** (int64) */
	processing: number
	/** (int64) */
	asyncProcessing: number
	/** (int64) */
	succeeded: number
	/** (int64) */
	failed: number
}
