package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 상품권 종류 */
@Serializable
public sealed class PaymentMethodGiftCertificateType {
  @SerialName("BOOKNLIFE")
  public data object Booknlife : PaymentMethodGiftCertificateType()
  @SerialName("SMART_MUNSANG")
  public data object SmartMunsang : PaymentMethodGiftCertificateType()
  @SerialName("CULTURELAND")
  public data object Cultureland : PaymentMethodGiftCertificateType()
  @SerialName("HAPPYMONEY")
  public data object Happymoney : PaymentMethodGiftCertificateType()
  @SerialName("CULTUREGIFT")
  public data object Culturegift : PaymentMethodGiftCertificateType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentMethodGiftCertificateType()
}
