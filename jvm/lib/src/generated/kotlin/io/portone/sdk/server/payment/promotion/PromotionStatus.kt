package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PromotionStatus {
  /** 예정됨 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PromotionStatus()
  /** 진행중 */
  @SerialName("IN_PROGRESS")
  public data object InProgress : PromotionStatus()
  /** 일시 중지됨 */
  @SerialName("PAUSED")
  public data object Paused : PromotionStatus()
  /** 예산 소진됨 */
  @SerialName("BUDGET_EXHAUSTED")
  public data object BudgetExhausted : PromotionStatus()
  /** 중단됨 */
  @SerialName("TERMINATED")
  public data object Terminated : PromotionStatus()
  /** 완료됨 */
  @SerialName("COMPLETED")
  public data object Completed : PromotionStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PromotionStatus()
}
