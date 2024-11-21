package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제건 내 현금영수증 상태 */
@Serializable
public sealed interface PaymentCashReceiptStatus {
  public val value: String
  @SerialName("ISSUED")
  public data object Issued : PaymentCashReceiptStatus {
    override val value: String = "ISSUED"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentCashReceiptStatus {
    override val value: String = "CANCELLED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentCashReceiptStatus
}
