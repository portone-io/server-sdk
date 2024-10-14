import type { BillingKeyPaymentMethod } from "#generated/payment/billingKey/BillingKeyPaymentMethod"
import type { SelectedChannel } from "#generated/common/SelectedChannel"

/** 빌링키 발급 성공 채널 응답 */
export type IssuedPgBillingKeyIssueResponse = {
	type: "ISSUED"
	/**
	 * 채널
	 *
	 * 빌링키 발급을 시도한 채널입니다.
	 */
	channel: SelectedChannel
	/** PG사 거래 아이디 */
	pgTxId?: string
	/**
	 * 빌링키 결제수단 상세 정보
	 *
	 * 채널에 대응되는 PG사에서 응답한 빌링키 발급 수단 정보입니다.
	 */
	method?: BillingKeyPaymentMethod
}
