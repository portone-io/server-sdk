package io.portone.sdk.server.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 채널 별 빌링키 발급 응답 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PgBillingKeyIssueResponse {
  /**
   * 채널
   *
   * 빌링키 발급을 시도한 채널입니다.
   */
  val channel: SelectedChannel
}
