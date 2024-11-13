package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 발급 유형 */
@Serializable
public sealed class InstantPaymentMethodInputVirtualAccountOptionType {
  /**
   * 회전식 가상계좌
   *
   * 일반적으로 사용되는 방식이며 PG사에서 직접 채번한 가상계좌번호를 사용합니다.
   */
  @SerialName("NORMAL")
  public data object Normal : InstantPaymentMethodInputVirtualAccountOptionType()
  /** 고정식 가상계좌 */
  @SerialName("FIXED")
  public data object Fixed : InstantPaymentMethodInputVirtualAccountOptionType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : InstantPaymentMethodInputVirtualAccountOptionType()
}
