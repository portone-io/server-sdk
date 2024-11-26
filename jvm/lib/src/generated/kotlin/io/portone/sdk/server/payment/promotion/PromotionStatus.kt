package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PromotionStatusSerializer::class)
public sealed interface PromotionStatus {
  public val value: String
  /** 예정됨 */
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PromotionStatus {
    override val value: String = "SCHEDULED"
  }
  private object ScheduledSerializer : KSerializer<Scheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scheduled = decoder.decodeString().let {
      if (it != "SCHEDULED") {
        throw SerializationException(it)
      } else {
        return Scheduled
      }
    }
    override fun serialize(encoder: Encoder, value: Scheduled) = encoder.encodeString(value.value)
  }
  /** 진행중 */
  @Serializable(InProgressSerializer::class)
  public data object InProgress : PromotionStatus {
    override val value: String = "IN_PROGRESS"
  }
  private object InProgressSerializer : KSerializer<InProgress> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InProgress::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InProgress = decoder.decodeString().let {
      if (it != "IN_PROGRESS") {
        throw SerializationException(it)
      } else {
        return InProgress
      }
    }
    override fun serialize(encoder: Encoder, value: InProgress) = encoder.encodeString(value.value)
  }
  /** 일시 중지됨 */
  @Serializable(PausedSerializer::class)
  public data object Paused : PromotionStatus {
    override val value: String = "PAUSED"
  }
  private object PausedSerializer : KSerializer<Paused> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paused::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paused = decoder.decodeString().let {
      if (it != "PAUSED") {
        throw SerializationException(it)
      } else {
        return Paused
      }
    }
    override fun serialize(encoder: Encoder, value: Paused) = encoder.encodeString(value.value)
  }
  /** 예산 소진됨 */
  @Serializable(BudgetExhaustedSerializer::class)
  public data object BudgetExhausted : PromotionStatus {
    override val value: String = "BUDGET_EXHAUSTED"
  }
  private object BudgetExhaustedSerializer : KSerializer<BudgetExhausted> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BudgetExhausted::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BudgetExhausted = decoder.decodeString().let {
      if (it != "BUDGET_EXHAUSTED") {
        throw SerializationException(it)
      } else {
        return BudgetExhausted
      }
    }
    override fun serialize(encoder: Encoder, value: BudgetExhausted) = encoder.encodeString(value.value)
  }
  /** 중단됨 */
  @Serializable(TerminatedSerializer::class)
  public data object Terminated : PromotionStatus {
    override val value: String = "TERMINATED"
  }
  private object TerminatedSerializer : KSerializer<Terminated> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Terminated::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Terminated = decoder.decodeString().let {
      if (it != "TERMINATED") {
        throw SerializationException(it)
      } else {
        return Terminated
      }
    }
    override fun serialize(encoder: Encoder, value: Terminated) = encoder.encodeString(value.value)
  }
  /** 완료됨 */
  @Serializable(CompletedSerializer::class)
  public data object Completed : PromotionStatus {
    override val value: String = "COMPLETED"
  }
  private object CompletedSerializer : KSerializer<Completed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Completed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Completed = decoder.decodeString().let {
      if (it != "COMPLETED") {
        throw SerializationException(it)
      } else {
        return Completed
      }
    }
    override fun serialize(encoder: Encoder, value: Completed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionStatus
}


private object PromotionStatusSerializer : KSerializer<PromotionStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionStatus::class.java.name, PrimitiveKind.STRING)
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
