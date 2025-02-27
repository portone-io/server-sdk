/** 분쟁 상태 */
export type DisputeStatus =
	/**
	 * 분쟁 발생 상태
	 *
	 * 분쟁이 발생하였으며 아직 해소되지 않은 상태입니다.
	 */
	| "UNRESOLVED"
	/**
	 * 분쟁 해소 상태
	 *
	 * 분쟁이 발생하였으나 해소된 상태입니다.
	 */
	| "RESOLVED"
	| string & {}
