package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제건 내 현금영수증 상태 */
@Serializable
public sealed class PaymentCashReceiptStatus {
  @SerialName("ISSUED")
  public data object Issued : PaymentCashReceiptStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentCashReceiptStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentCashReceiptStatus()
}
