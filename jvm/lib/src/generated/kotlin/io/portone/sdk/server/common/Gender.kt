package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 성별 */
@Serializable
public sealed interface Gender {
  public val value: String
  /** 남성 */
  @SerialName("MALE")
  public data object Male : Gender {
    override val value: String = "MALE"
  }
  /** 여성 */
  @SerialName("FEMALE")
  public data object Female : Gender {
    override val value: String = "FEMALE"
  }
  /** 그 외 성별 */
  @SerialName("OTHER")
  public data object Other : Gender {
    override val value: String = "OTHER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Gender
}
