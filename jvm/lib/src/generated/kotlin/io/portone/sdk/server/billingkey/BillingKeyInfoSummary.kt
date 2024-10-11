package io.portone.sdk.server.billingkey

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class BillingKeyInfoSummary(
  /** 발급된 빌링키 */
  val billingKey: String,
  /** 빌링크 발급 완료 시점 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant,
  /** 발급된 채널 */
  val channels: List<SelectedChannel>? = null,
)