package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 카드 소유주 유형 */
@Serializable
public enum class CardOwnerType {
  /** 개인 */
  PERSONAL,
  /** 법인 */
  CORPORATE,
}
