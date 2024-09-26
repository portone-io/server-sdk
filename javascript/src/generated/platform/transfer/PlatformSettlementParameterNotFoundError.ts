/** 정산 파라미터가 존재하지 않는 경우 */
export type PlatformSettlementParameterNotFoundError = {
	type: "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND"
	message?: string
}
