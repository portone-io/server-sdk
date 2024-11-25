package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PromotionStatusSerializer::class)
public sealed interface PromotionStatus {
  public val value: String
  /** 예정됨 */
  public data object Scheduled : PromotionStatus {
    override val value: String = "SCHEDULED"
  }
  /** 진행중 */
  public data object InProgress : PromotionStatus {
    override val value: String = "IN_PROGRESS"
  }
  /** 일시 중지됨 */
  public data object Paused : PromotionStatus {
    override val value: String = "PAUSED"
  }
  /** 예산 소진됨 */
  public data object BudgetExhausted : PromotionStatus {
    override val value: String = "BUDGET_EXHAUSTED"
  }
  /** 중단됨 */
  public data object Terminated : PromotionStatus {
    override val value: String = "TERMINATED"
  }
  /** 완료됨 */
  public data object Completed : PromotionStatus {
    override val value: String = "COMPLETED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionStatus
}


private object PromotionStatusSerializer : KSerializer<PromotionStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PromotionStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PromotionStatus.Scheduled
      "IN_PROGRESS" -> PromotionStatus.InProgress
      "PAUSED" -> PromotionStatus.Paused
      "BUDGET_EXHAUSTED" -> PromotionStatus.BudgetExhausted
      "TERMINATED" -> PromotionStatus.Terminated
      "COMPLETED" -> PromotionStatus.Completed
      else -> PromotionStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PromotionStatus) = encoder.encodeString(value.value)
}
