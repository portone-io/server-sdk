package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건 상태 */
@Serializable
public sealed interface PaymentStatus {
  public val value: String
  @SerialName("READY")
  public data object Ready : PaymentStatus {
    override val value: String = "READY"
  }
  @SerialName("PENDING")
  public data object Pending : PaymentStatus {
    override val value: String = "PENDING"
  }
  @SerialName("VIRTUAL_ACCOUNT_ISSUED")
  public data object VirtualAccountIssued : PaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  @SerialName("PAID")
  public data object Paid : PaymentStatus {
    override val value: String = "PAID"
  }
  @SerialName("FAILED")
  public data object Failed : PaymentStatus {
    override val value: String = "FAILED"
  }
  @SerialName("PARTIAL_CANCELLED")
  public data object PartialCancelled : PaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentStatus {
    override val value: String = "CANCELLED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentStatus
}
