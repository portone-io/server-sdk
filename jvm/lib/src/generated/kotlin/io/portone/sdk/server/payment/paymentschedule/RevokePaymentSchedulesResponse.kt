package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 예약 건 취소 성공 응답 */
@Serializable
public data class RevokePaymentSchedulesResponse(
  /** 취소 완료된 결제 예약 건 아이디 목록 */
  val revokedScheduleIds: List<String>,
  /** 결제 예약 건 취소 완료 시점 */
  val revokedAt: @Serializable(InstantSerializer::class) Instant? = null,
)


