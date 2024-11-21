package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금액에 대한 소수점 처리 방식 */
@Serializable
public sealed interface PlatformRoundType {
  public val value: String
  /** 소수점 반올림 */
  @SerialName("OFF")
  public data object Off : PlatformRoundType {
    override val value: String = "OFF"
  }
  /** 소수점 내림 */
  @SerialName("DOWN")
  public data object Down : PlatformRoundType {
    override val value: String = "DOWN"
  }
  /** 소수점 올림 */
  @SerialName("UP")
  public data object Up : PlatformRoundType {
    override val value: String = "UP"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformRoundType
}
