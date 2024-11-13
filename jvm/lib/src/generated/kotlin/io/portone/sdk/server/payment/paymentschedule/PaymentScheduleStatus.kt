package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약 건 상태 */
@Serializable
public sealed class PaymentScheduleStatus {
  /** 예약 완료 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PaymentScheduleStatus()
  /** 결제 시작 */
  @SerialName("STARTED")
  public data object Started : PaymentScheduleStatus()
  /** 결제 성공 */
  @SerialName("SUCCEEDED")
  public data object Succeeded : PaymentScheduleStatus()
  /** 결제 실패 */
  @SerialName("FAILED")
  public data object Failed : PaymentScheduleStatus()
  /** 취소된 결제 예약 */
  @SerialName("REVOKED")
  public data object Revoked : PaymentScheduleStatus()
  /** 결제 승인 대기 */
  @SerialName("PENDING")
  public data object Pending : PaymentScheduleStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentScheduleStatus()
}
