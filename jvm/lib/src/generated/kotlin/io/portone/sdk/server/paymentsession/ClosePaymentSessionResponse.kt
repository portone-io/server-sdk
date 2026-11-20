package io.portone.sdk.server.paymentsession

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 결제 세션 종료 성공 응답 */
@Serializable
public data class ClosePaymentSessionResponse(
  /** 결제 세션 종료 시각 */
  val closedAt: @Serializable(InstantSerializer::class) Instant,
)


