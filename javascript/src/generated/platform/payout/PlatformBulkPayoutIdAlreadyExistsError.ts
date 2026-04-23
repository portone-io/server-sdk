/** 일괄 지급 아이디가 이미 존재하는 경우 */
export type PlatformBulkPayoutIdAlreadyExistsError = {
	type: "PLATFORM_BULK_PAYOUT_ID_ALREADY_EXISTS"
	message?: string
}
