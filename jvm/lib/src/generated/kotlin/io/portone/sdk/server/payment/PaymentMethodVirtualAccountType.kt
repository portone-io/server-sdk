package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 유형 */
@Serializable
public sealed interface PaymentMethodVirtualAccountType {
  public val value: String
  /** 고정식 */
  @SerialName("FIXED")
  public data object Fixed : PaymentMethodVirtualAccountType {
    override val value: String = "FIXED"
  }
  /** 회전식 */
  @SerialName("NORMAL")
  public data object Normal : PaymentMethodVirtualAccountType {
    override val value: String = "NORMAL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountType
}
