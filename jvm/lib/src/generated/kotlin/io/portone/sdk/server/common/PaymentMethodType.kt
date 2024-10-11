package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

@Serializable
public enum class PaymentMethodType {
  CARD,
  TRANSFER,
  VIRTUAL_ACCOUNT,
  GIFT_CERTIFICATE,
  MOBILE,
  EASY_PAY,
}
