package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 금액에 대한 소수점 처리 방식 */
@Serializable
public enum class PlatformRoundType {
  /** 소수점 반올림 */
  Off,
  /** 소수점 내림 */
  Down,
  /** 소수점 올림 */
  Up,
}
