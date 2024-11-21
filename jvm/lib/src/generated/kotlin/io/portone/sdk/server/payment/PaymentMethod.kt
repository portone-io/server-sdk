package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제수단 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PaymentMethod {
  public sealed interface Recognized : PaymentMethod {
  }
  public data object Unrecognized : PaymentMethod
}
