package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 파트너 유형별 추가 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPartnerType {
  public sealed interface Recognized : PlatformPartnerType {
  }
  public data object Unrecognized : PlatformPartnerType
}
