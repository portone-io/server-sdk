package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 유형 */
@Serializable
public sealed interface CardType {
  public val value: String
  /** 신용카드 */
  @SerialName("CREDIT")
  public data object Credit : CardType {
    override val value: String = "CREDIT"
  }
  /** 체크카드 */
  @SerialName("DEBIT")
  public data object Debit : CardType {
    override val value: String = "DEBIT"
  }
  /** 기프트카드 */
  @SerialName("GIFT")
  public data object Gift : CardType {
    override val value: String = "GIFT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardType
}
