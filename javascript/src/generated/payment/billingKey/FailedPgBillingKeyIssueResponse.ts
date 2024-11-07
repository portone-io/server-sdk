import type { BillingKeyFailure } from "./../../payment/billingKey/BillingKeyFailure"
import type { SelectedChannel } from "./../../common/SelectedChannel"

/** 빌링키 발급 실패 채널 응답 */
export type FailedPgBillingKeyIssueResponse = {
	type: "FAILED"
	/**
	 * 채널
	 *
	 * 빌링키 발급을 시도한 채널입니다.
	 */
	channel: SelectedChannel
	/** 발급 실패 상세 정보 */
	failure: BillingKeyFailure
}
