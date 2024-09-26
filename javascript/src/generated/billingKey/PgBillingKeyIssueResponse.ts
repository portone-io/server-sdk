import type { FailedPgBillingKeyIssueResponse } from "#generated/billingKey/FailedPgBillingKeyIssueResponse"
import type { IssuedPgBillingKeyIssueResponse } from "#generated/billingKey/IssuedPgBillingKeyIssueResponse"

/** 채널 별 빌링키 발급 응답 */
export type PgBillingKeyIssueResponse =
	/** 발급 실패 채널 응답 */
	| FailedPgBillingKeyIssueResponse
	/** 발급 성공 채널 응답 */
	| IssuedPgBillingKeyIssueResponse
