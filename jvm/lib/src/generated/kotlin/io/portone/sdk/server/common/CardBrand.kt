package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 브랜드 */
@Serializable
public sealed interface CardBrand {
  public val value: String
  @SerialName("LOCAL")
  public data object Local : CardBrand {
    override val value: String = "LOCAL"
  }
  @SerialName("MASTER")
  public data object Master : CardBrand {
    override val value: String = "MASTER"
  }
  @SerialName("UNIONPAY")
  public data object Unionpay : CardBrand {
    override val value: String = "UNIONPAY"
  }
  @SerialName("VISA")
  public data object Visa : CardBrand {
    override val value: String = "VISA"
  }
  @SerialName("JCB")
  public data object Jcb : CardBrand {
    override val value: String = "JCB"
  }
  @SerialName("AMEX")
  public data object Amex : CardBrand {
    override val value: String = "AMEX"
  }
  @SerialName("DINERS")
  public data object Diners : CardBrand {
    override val value: String = "DINERS"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardBrand
}
