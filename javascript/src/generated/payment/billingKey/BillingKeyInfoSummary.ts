import type { SelectedChannel } from "#generated/common/SelectedChannel"

export type BillingKeyInfoSummary = {
	/** 발급된 빌링키 */
	billingKey: string
	/** 발급된 채널 */
	channels?: SelectedChannel[]
	/**
	 * 빌링크 발급 완료 시점
	 * (RFC 3339 date-time)
	 */
	issuedAt: string
}
