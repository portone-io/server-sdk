package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 수단 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPaymentMethod {
  public sealed interface Recognized : PlatformPaymentMethod {
  }
  public data object Unrecognized : PlatformPaymentMethod
}
