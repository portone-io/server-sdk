package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PaymentMethodType {
  @SerialName("CARD")
  public data object Card : PaymentMethodType()
  @SerialName("TRANSFER")
  public data object Transfer : PaymentMethodType()
  @SerialName("VIRTUAL_ACCOUNT")
  public data object VirtualAccount : PaymentMethodType()
  @SerialName("GIFT_CERTIFICATE")
  public data object GiftCertificate : PaymentMethodType()
  @SerialName("MOBILE")
  public data object Mobile : PaymentMethodType()
  @SerialName("EASY_PAY")
  public data object EasyPay : PaymentMethodType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentMethodType()
}
