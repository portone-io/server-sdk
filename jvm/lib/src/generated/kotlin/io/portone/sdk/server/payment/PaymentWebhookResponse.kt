package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 웹훅 응답 정보 */
@Serializable
public data class PaymentWebhookResponse(
  /** 응답 HTTP 코드 */
  val code: String,
  /** 응답 헤더 */
  val header: String,
  /** 응답 본문 */
  val body: String,
  /** 응답 시점 */
  val respondedAt: @Serializable(InstantSerializer::class) Instant,
)


