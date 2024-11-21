package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PromotionStatus {
  public val value: String
  /** 예정됨 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PromotionStatus {
    override val value: String = "SCHEDULED"
  }
  /** 진행중 */
  @SerialName("IN_PROGRESS")
  public data object InProgress : PromotionStatus {
    override val value: String = "IN_PROGRESS"
  }
  /** 일시 중지됨 */
  @SerialName("PAUSED")
  public data object Paused : PromotionStatus {
    override val value: String = "PAUSED"
  }
  /** 예산 소진됨 */
  @SerialName("BUDGET_EXHAUSTED")
  public data object BudgetExhausted : PromotionStatus {
    override val value: String = "BUDGET_EXHAUSTED"
  }
  /** 중단됨 */
  @SerialName("TERMINATED")
  public data object Terminated : PromotionStatus {
    override val value: String = "TERMINATED"
  }
  /** 완료됨 */
  @SerialName("COMPLETED")
  public data object Completed : PromotionStatus {
    override val value: String = "COMPLETED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionStatus
}
