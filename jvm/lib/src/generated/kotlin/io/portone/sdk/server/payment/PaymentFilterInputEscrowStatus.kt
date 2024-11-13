package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 에스크로 상태 */
@Serializable
public sealed class PaymentFilterInputEscrowStatus {
  @SerialName("REGISTERED")
  public data object Registered : PaymentFilterInputEscrowStatus()
  @SerialName("DELIVERED")
  public data object Delivered : PaymentFilterInputEscrowStatus()
  @SerialName("CONFIRMED")
  public data object Confirmed : PaymentFilterInputEscrowStatus()
  @SerialName("REJECTED")
  public data object Rejected : PaymentFilterInputEscrowStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentFilterInputEscrowStatus()
  @SerialName("REJECT_CONFIRMED")
  public data object RejectConfirmed : PaymentFilterInputEscrowStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentFilterInputEscrowStatus()
}
