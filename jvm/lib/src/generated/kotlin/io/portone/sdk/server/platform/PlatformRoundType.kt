package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금액에 대한 소수점 처리 방식 */
@Serializable
public sealed class PlatformRoundType {
  /** 소수점 반올림 */
  @SerialName("OFF")
  public data object Off : PlatformRoundType()
  /** 소수점 내림 */
  @SerialName("DOWN")
  public data object Down : PlatformRoundType()
  /** 소수점 올림 */
  @SerialName("UP")
  public data object Up : PlatformRoundType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformRoundType()
}
