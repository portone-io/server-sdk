package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 브랜드 */
@Serializable
public sealed class CardBrand {
  @SerialName("LOCAL")
  public data object Local : CardBrand()
  @SerialName("MASTER")
  public data object Master : CardBrand()
  @SerialName("UNIONPAY")
  public data object Unionpay : CardBrand()
  @SerialName("VISA")
  public data object Visa : CardBrand()
  @SerialName("JCB")
  public data object Jcb : CardBrand()
  @SerialName("AMEX")
  public data object Amex : CardBrand()
  @SerialName("DINERS")
  public data object Diners : CardBrand()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : CardBrand()
}
