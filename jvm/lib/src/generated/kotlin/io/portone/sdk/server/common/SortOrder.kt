package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정렬 방식 */
@Serializable
public sealed interface SortOrder {
  public val value: String
  /** 내림차순 */
  @SerialName("DESC")
  public data object Desc : SortOrder {
    override val value: String = "DESC"
  }
  /** 오름차순 */
  @SerialName("ASC")
  public data object Asc : SortOrder {
    override val value: String = "ASC"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SortOrder
}
