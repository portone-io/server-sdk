/** 본인인증 내역 정렬 기준 */
export type IdentityVerificationSortBy =
	/** 요청 시각 */
	| "REQUESTED_AT"
	/** 완료 시각 */
	| "VERIFIED_AT"
	/** 실패 시각 */
	| "FAILED_AT"
	/**
	 * 상태 변경 시각
	 *
	 * 요청 상태의 경우 REQUESTED_AT, 완료 상태의 경우 VERIFIED_AT, 실패 상태의 경우 FAILED_AT
	 */
	| "STATUS_UPDATED_AT"
	| string & {}
