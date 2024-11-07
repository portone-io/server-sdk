package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 상품권 종류 */
@Serializable
public enum class PaymentMethodGiftCertificateType {
  Booknlife,
  SmartMunsang,
  Cultureland,
  Happymoney,
  Culturegift,
}
