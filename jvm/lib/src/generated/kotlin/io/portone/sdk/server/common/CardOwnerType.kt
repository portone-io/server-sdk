package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 소유주 유형 */
@Serializable
public sealed interface CardOwnerType {
  public val value: String
  /** 개인 */
  @SerialName("PERSONAL")
  public data object Personal : CardOwnerType {
    override val value: String = "PERSONAL"
  }
  /** 법인 */
  @SerialName("CORPORATE")
  public data object Corporate : CardOwnerType {
    override val value: String = "CORPORATE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardOwnerType
}
