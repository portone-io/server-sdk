package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 채널 타입 */
@Serializable
public sealed interface SelectedChannelType {
  public val value: String
  /** 실 연동 채널 */
  @SerialName("LIVE")
  public data object Live : SelectedChannelType {
    override val value: String = "LIVE"
  }
  /** 테스트 연동 채널 */
  @SerialName("TEST")
  public data object Test : SelectedChannelType {
    override val value: String = "TEST"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SelectedChannelType
}
