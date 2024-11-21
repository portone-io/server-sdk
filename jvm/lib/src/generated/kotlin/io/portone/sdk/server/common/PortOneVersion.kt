package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 포트원 버전 */
@Serializable
public sealed interface PortOneVersion {
  public val value: String
  @SerialName("V1")
  public data object V1 : PortOneVersion {
    override val value: String = "V1"
  }
  @SerialName("V2")
  public data object V2 : PortOneVersion {
    override val value: String = "V2"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PortOneVersion
}
