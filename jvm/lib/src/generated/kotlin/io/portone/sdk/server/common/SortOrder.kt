package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정렬 방식 */
@Serializable
public sealed class SortOrder {
  /** 내림차순 */
  @SerialName("DESC")
  public data object Desc : SortOrder()
  /** 오름차순 */
  @SerialName("ASC")
  public data object Asc : SortOrder()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : SortOrder()
}
