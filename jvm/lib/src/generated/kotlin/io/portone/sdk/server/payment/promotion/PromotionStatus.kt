package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable

@Serializable
public enum class PromotionStatus {
  /** 예정됨 */
  Scheduled,
  /** 진행중 */
  InProgress,
  /** 일시 중지됨 */
  Paused,
  /** 예산 소진됨 */
  BudgetExhausted,
  /** 중단됨 */
  Terminated,
  /** 완료됨 */
  Completed,
}
