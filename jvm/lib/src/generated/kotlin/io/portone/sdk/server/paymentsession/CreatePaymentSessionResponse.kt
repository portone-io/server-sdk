package io.portone.sdk.server.paymentsession

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 세션 생성 성공 응답 */
@Serializable
public data class CreatePaymentSessionResponse(
  /** 세션 아이디 */
  val sessionId: String,
  /** 호스티드 체크아웃 페이지 URL */
  val url: String,
  /** 만료 시각 */
  val expiresAt: @Serializable(InstantSerializer::class) Instant,
)


