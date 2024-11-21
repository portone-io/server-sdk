package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 에스크로 상태 */
@Serializable
public sealed interface PaymentFilterInputEscrowStatus {
  public val value: String
  @SerialName("REGISTERED")
  public data object Registered : PaymentFilterInputEscrowStatus {
    override val value: String = "REGISTERED"
  }
  @SerialName("DELIVERED")
  public data object Delivered : PaymentFilterInputEscrowStatus {
    override val value: String = "DELIVERED"
  }
  @SerialName("CONFIRMED")
  public data object Confirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "CONFIRMED"
  }
  @SerialName("REJECTED")
  public data object Rejected : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECTED"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentFilterInputEscrowStatus {
    override val value: String = "CANCELLED"
  }
  @SerialName("REJECT_CONFIRMED")
  public data object RejectConfirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECT_CONFIRMED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentFilterInputEscrowStatus
}
