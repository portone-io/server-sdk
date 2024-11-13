package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 환불 상태 */
@Serializable
public sealed class PaymentMethodVirtualAccountRefundStatus {
  /** 처리중 */
  @SerialName("PENDING")
  public data object Pending : PaymentMethodVirtualAccountRefundStatus()
  /** 부분 환불 실패 */
  @SerialName("PARTIAL_REFUND_FAILED")
  public data object PartialRefundFailed : PaymentMethodVirtualAccountRefundStatus()
  /** 환불 실패 */
  @SerialName("FAILED")
  public data object Failed : PaymentMethodVirtualAccountRefundStatus()
  /** 환불 완료 */
  @SerialName("COMPLETED")
  public data object Completed : PaymentMethodVirtualAccountRefundStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentMethodVirtualAccountRefundStatus()
}
