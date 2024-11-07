import type { SelectedChannel } from "./../../common/SelectedChannel"

/** 발급 실패 */
export type IssueFailedCashReceipt = {
	/** 현금영수증 상태 */
	status: "ISSUE_FAILED"
	/** 고객사 아이디 */
	merchantId: string
	/** 상점 아이디 */
	storeId: string
	/** 결제 건 아이디 */
	paymentId: string
	/** 현금영수증 발급에 사용된 채널 */
	channel?: SelectedChannel
	/** 주문명 */
	orderName: string
	/** 수동 발급 여부 */
	isManual: boolean
}
