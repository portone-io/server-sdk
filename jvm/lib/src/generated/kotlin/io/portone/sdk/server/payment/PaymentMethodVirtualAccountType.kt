package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 유형 */
@Serializable
public sealed class PaymentMethodVirtualAccountType {
  /** 고정식 */
  @SerialName("FIXED")
  public data object Fixed : PaymentMethodVirtualAccountType()
  /** 회전식 */
  @SerialName("NORMAL")
  public data object Normal : PaymentMethodVirtualAccountType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentMethodVirtualAccountType()
}
