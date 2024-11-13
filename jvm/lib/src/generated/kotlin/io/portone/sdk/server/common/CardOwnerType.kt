package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 소유주 유형 */
@Serializable
public sealed class CardOwnerType {
  /** 개인 */
  @SerialName("PERSONAL")
  public data object Personal : CardOwnerType()
  /** 법인 */
  @SerialName("CORPORATE")
  public data object Corporate : CardOwnerType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : CardOwnerType()
}
