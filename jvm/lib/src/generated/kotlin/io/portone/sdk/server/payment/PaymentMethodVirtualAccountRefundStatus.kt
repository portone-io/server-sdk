package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 환불 상태 */
@Serializable
public sealed interface PaymentMethodVirtualAccountRefundStatus {
  public val value: String
  /** 처리중 */
  @SerialName("PENDING")
  public data object Pending : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "PENDING"
  }
  /** 부분 환불 실패 */
  @SerialName("PARTIAL_REFUND_FAILED")
  public data object PartialRefundFailed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "PARTIAL_REFUND_FAILED"
  }
  /** 환불 실패 */
  @SerialName("FAILED")
  public data object Failed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "FAILED"
  }
  /** 환불 완료 */
  @SerialName("COMPLETED")
  public data object Completed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "COMPLETED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountRefundStatus
}
