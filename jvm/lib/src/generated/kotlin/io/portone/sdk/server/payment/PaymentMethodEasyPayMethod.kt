package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 간편 결제 수단 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PaymentMethodEasyPayMethod {
  public sealed interface Recognized : PaymentMethodEasyPayMethod {
  }
  public data object Unrecognized : PaymentMethodEasyPayMethod
}
