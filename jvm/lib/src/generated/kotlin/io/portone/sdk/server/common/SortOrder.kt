package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 정렬 방식 */
@Serializable
public enum class SortOrder {
  /** 내림차순 */
  DESC,
  /** 오름차순 */
  ASC,
}
