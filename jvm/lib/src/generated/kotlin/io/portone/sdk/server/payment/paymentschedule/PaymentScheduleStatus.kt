package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약 건 상태 */
@Serializable
public sealed interface PaymentScheduleStatus {
  public val value: String
  /** 예약 완료 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PaymentScheduleStatus {
    override val value: String = "SCHEDULED"
  }
  /** 결제 시작 */
  @SerialName("STARTED")
  public data object Started : PaymentScheduleStatus {
    override val value: String = "STARTED"
  }
  /** 결제 성공 */
  @SerialName("SUCCEEDED")
  public data object Succeeded : PaymentScheduleStatus {
    override val value: String = "SUCCEEDED"
  }
  /** 결제 실패 */
  @SerialName("FAILED")
  public data object Failed : PaymentScheduleStatus {
    override val value: String = "FAILED"
  }
  /** 취소된 결제 예약 */
  @SerialName("REVOKED")
  public data object Revoked : PaymentScheduleStatus {
    override val value: String = "REVOKED"
  }
  /** 결제 승인 대기 */
  @SerialName("PENDING")
  public data object Pending : PaymentScheduleStatus {
    override val value: String = "PENDING"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleStatus
}
