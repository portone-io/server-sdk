package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 유형 */
@Serializable
public sealed class CardType {
  /** 신용카드 */
  @SerialName("CREDIT")
  public data object Credit : CardType()
  /** 체크카드 */
  @SerialName("DEBIT")
  public data object Debit : CardType()
  /** 기프트카드 */
  @SerialName("GIFT")
  public data object Gift : CardType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : CardType()
}
