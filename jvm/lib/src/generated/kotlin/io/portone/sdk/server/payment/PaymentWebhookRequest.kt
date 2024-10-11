package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 웹훅 요청 정보 */
@Serializable
public data class PaymentWebhookRequest(
  /** 요청 본문 */
  val body: String,
  /** 요청 헤더 */
  val header: String? = null,
  /** 요청 시점 */
  val requestedAt: @Serializable(InstantSerializer::class) Instant? = null,
)
