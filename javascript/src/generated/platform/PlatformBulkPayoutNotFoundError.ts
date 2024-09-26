/** 일괄 지급이 존재하지 않는 경우 */
export type PlatformBulkPayoutNotFoundError = {
	type: "PLATFORM_BULK_PAYOUT_NOT_FOUND"
	message?: string
}
