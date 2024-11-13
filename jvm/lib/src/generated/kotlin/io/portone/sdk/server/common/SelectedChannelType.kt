package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 채널 타입 */
@Serializable
public sealed class SelectedChannelType {
  /** 실 연동 채널 */
  @SerialName("LIVE")
  public data object Live : SelectedChannelType()
  /** 테스트 연동 채널 */
  @SerialName("TEST")
  public data object Test : SelectedChannelType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : SelectedChannelType()
}
