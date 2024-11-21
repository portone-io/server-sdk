package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 상품권 종류 */
@Serializable
public sealed interface PaymentMethodGiftCertificateType {
  public val value: String
  @SerialName("BOOKNLIFE")
  public data object Booknlife : PaymentMethodGiftCertificateType {
    override val value: String = "BOOKNLIFE"
  }
  @SerialName("SMART_MUNSANG")
  public data object SmartMunsang : PaymentMethodGiftCertificateType {
    override val value: String = "SMART_MUNSANG"
  }
  @SerialName("CULTURELAND")
  public data object Cultureland : PaymentMethodGiftCertificateType {
    override val value: String = "CULTURELAND"
  }
  @SerialName("HAPPYMONEY")
  public data object Happymoney : PaymentMethodGiftCertificateType {
    override val value: String = "HAPPYMONEY"
  }
  @SerialName("CULTUREGIFT")
  public data object Culturegift : PaymentMethodGiftCertificateType {
    override val value: String = "CULTUREGIFT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodGiftCertificateType
}
