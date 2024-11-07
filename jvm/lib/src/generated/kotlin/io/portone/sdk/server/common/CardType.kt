package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 카드 유형 */
@Serializable
public enum class CardType {
  /** 신용카드 */
  Credit,
  /** 체크카드 */
  Debit,
  /** 기프트카드 */
  Gift,
}
