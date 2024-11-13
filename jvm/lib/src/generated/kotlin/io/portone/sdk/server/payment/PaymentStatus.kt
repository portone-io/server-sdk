package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건 상태 */
@Serializable
public sealed class PaymentStatus {
  @SerialName("READY")
  public data object Ready : PaymentStatus()
  @SerialName("PENDING")
  public data object Pending : PaymentStatus()
  @SerialName("VIRTUAL_ACCOUNT_ISSUED")
  public data object VirtualAccountIssued : PaymentStatus()
  @SerialName("PAID")
  public data object Paid : PaymentStatus()
  @SerialName("FAILED")
  public data object Failed : PaymentStatus()
  @SerialName("PARTIAL_CANCELLED")
  public data object PartialCancelled : PaymentStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentStatus()
}
