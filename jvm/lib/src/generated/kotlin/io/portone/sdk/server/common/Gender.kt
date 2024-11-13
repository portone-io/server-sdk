package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 성별 */
@Serializable
public sealed class Gender {
  /** 남성 */
  @SerialName("MALE")
  public data object Male : Gender()
  /** 여성 */
  @SerialName("FEMALE")
  public data object Female : Gender()
  /** 그 외 성별 */
  @SerialName("OTHER")
  public data object Other : Gender()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : Gender()
}
