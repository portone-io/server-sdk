package io.portone.sdk.server.paymentschedule

import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 예약 건 취소 성공 응답 */
@Serializable
public data class RevokePaymentSchedulesResponse(
  /** 취소 완료된 결제 예약 건 아이디 목록 */
  val revokedScheduleIds: Array<String>,
  /** 결제 예약 건 취소 완료 시점 */
  val revokedAt: Instant? = null,
)
