package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 포트원 버전 */
@Serializable
public sealed class PortOneVersion {
  @SerialName("V1")
  public data object V1 : PortOneVersion()
  @SerialName("V2")
  public data object V2 : PortOneVersion()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PortOneVersion()
}
