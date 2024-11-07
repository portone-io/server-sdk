package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

@Serializable
public enum class PaymentMethodType {
  Card,
  Transfer,
  VirtualAccount,
  GiftCertificate,
  Mobile,
  EasyPay,
}
