import type { BillingKeyInfoSummary } from "#generated/payment/billingKey/BillingKeyInfoSummary"
import type { ChannelSpecificFailure } from "#generated/payment/billingKey/ChannelSpecificFailure"

/** 빌링키 발급 성공 응답 */
export type IssueBillingKeyResponse = {
	/** 빌링키 정보 */
	billingKeyInfo: BillingKeyInfoSummary
	/** 발급에 실패한 채널이 있을시 실패 정보 */
	channelSpecificFailures?: ChannelSpecificFailure[]
}
