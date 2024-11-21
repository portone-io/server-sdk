package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 플랫폼 중개수수료 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformFee {
  public sealed interface Recognized : PlatformFee {
  }
  public data object Unrecognized : PlatformFee
}
