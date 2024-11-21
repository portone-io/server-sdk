package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 상태 */
@Serializable
public sealed interface BillingKeyStatus {
  public val value: String
  @SerialName("ISSUED")
  public data object Issued : BillingKeyStatus {
    override val value: String = "ISSUED"
  }
  @SerialName("DELETED")
  public data object Deleted : BillingKeyStatus {
    override val value: String = "DELETED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyStatus
}
