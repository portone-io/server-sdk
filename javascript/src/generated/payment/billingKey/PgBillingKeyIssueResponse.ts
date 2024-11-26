import type { Unrecognized } from "./../../../utils/unrecognized"
import type { FailedPgBillingKeyIssueResponse } from "./../../payment/billingKey/FailedPgBillingKeyIssueResponse"
import type { IssuedPgBillingKeyIssueResponse } from "./../../payment/billingKey/IssuedPgBillingKeyIssueResponse"
/** 채널 별 빌링키 발급 응답 */
export type PgBillingKeyIssueResponse =
	/** 발급 실패 채널 응답 */
	| FailedPgBillingKeyIssueResponse
	/** 발급 성공 채널 응답 */
	| IssuedPgBillingKeyIssueResponse
	| { readonly type: Unrecognized }

export function isUnrecognizedPgBillingKeyIssueResponse(entity: PgBillingKeyIssueResponse): entity is { readonly type: Unrecognized } {
	return entity.type !== "FAILED"
		&& entity.type !== "ISSUED"
}
