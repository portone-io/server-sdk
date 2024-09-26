/** 가상계좌 말소 성공 응답 */
export type CloseVirtualAccountResponse = {
	/**
	 * 가상계좌 말소 시점
	 * (RFC 3339 date-time)
	 */
	closedAt: string
}
