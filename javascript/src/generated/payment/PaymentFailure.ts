/** 결제 실패 정보 */
export type PaymentFailure = {
	/** 실패 사유 */
	reason?: string
	/** PG사 실패 코드 */
	pgCode?: string
	/** PG사 실패 메시지 */
	pgMessage?: string
}