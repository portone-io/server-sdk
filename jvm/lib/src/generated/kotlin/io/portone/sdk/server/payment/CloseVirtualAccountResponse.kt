package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 가상계좌 말소 성공 응답 */
@Serializable
public data class CloseVirtualAccountResponse(
  /** 가상계좌 말소 시점 */
  val closedAt: @Serializable(InstantSerializer::class) Instant,
)
