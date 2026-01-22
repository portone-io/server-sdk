package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 결제 취소 요청 취소 성공 응답 */
@Serializable
public data class StopPaymentCancellationResponse(
  /** 결제 취소 요청 취소 완료 시각 */
  val stoppedAt: @Serializable(InstantSerializer::class) Instant,
)


