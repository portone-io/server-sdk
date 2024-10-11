package io.portone.sdk.server.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

@Serializable
public data class BillingKeyInfoSummary(
  /** 발급된 빌링키 */
  val billingKey: String,
  /** 빌링크 발급 완료 시점 */
  val issuedAt: Instant,
  /** 발급된 채널 */
  val channels: Array<SelectedChannel>? = null,
)
