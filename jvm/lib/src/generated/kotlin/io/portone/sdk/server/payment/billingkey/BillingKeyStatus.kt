package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 상태 */
@Serializable
public sealed class BillingKeyStatus {
  @SerialName("ISSUED")
  public data object Issued : BillingKeyStatus()
  @SerialName("DELETED")
  public data object Deleted : BillingKeyStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : BillingKeyStatus()
}
