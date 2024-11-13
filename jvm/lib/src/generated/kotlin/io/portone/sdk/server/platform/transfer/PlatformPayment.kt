package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPayment {
  public data object Unrecognized : PlatformPayment
}
