package io.portone.sdk.server.payment.paymentschedule

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약 건 정렬 기준 */
@Serializable
public sealed interface PaymentScheduleSortBy {
  public val value: String
  /** 결제 예약 생성 시각 */
  @SerialName("CREATED_AT")
  public data object CreatedAt : PaymentScheduleSortBy {
    override val value: String = "CREATED_AT"
  }
  /** 결제 예정 시각 */
  @SerialName("TIME_TO_PAY")
  public data object TimeToPay : PaymentScheduleSortBy {
    override val value: String = "TIME_TO_PAY"
  }
  /** 예약 결제 시도(성공 / 실패) 시각 */
  @SerialName("COMPLETED_AT")
  public data object CompletedAt : PaymentScheduleSortBy {
    override val value: String = "COMPLETED_AT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentScheduleSortBy
}
