package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 성별 */
@Serializable
public enum class Gender {
  /** 남성 */
  Male,
  /** 여성 */
  Female,
  /** 그 외 성별 */
  Other,
}
