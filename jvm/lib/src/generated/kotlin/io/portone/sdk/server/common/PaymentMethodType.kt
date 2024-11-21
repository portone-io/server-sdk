package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PaymentMethodType {
  public val value: String
  @SerialName("CARD")
  public data object Card : PaymentMethodType {
    override val value: String = "CARD"
  }
  @SerialName("TRANSFER")
  public data object Transfer : PaymentMethodType {
    override val value: String = "TRANSFER"
  }
  @SerialName("VIRTUAL_ACCOUNT")
  public data object VirtualAccount : PaymentMethodType {
    override val value: String = "VIRTUAL_ACCOUNT"
  }
  @SerialName("GIFT_CERTIFICATE")
  public data object GiftCertificate : PaymentMethodType {
    override val value: String = "GIFT_CERTIFICATE"
  }
  @SerialName("MOBILE")
  public data object Mobile : PaymentMethodType {
    override val value: String = "MOBILE"
  }
  @SerialName("EASY_PAY")
  public data object EasyPay : PaymentMethodType {
    override val value: String = "EASY_PAY"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodType
}
