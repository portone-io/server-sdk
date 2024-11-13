package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 채널 별 빌링키 발급 응답 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PgBillingKeyIssueResponse {
  public data object Unrecognized : PgBillingKeyIssueResponse
}
