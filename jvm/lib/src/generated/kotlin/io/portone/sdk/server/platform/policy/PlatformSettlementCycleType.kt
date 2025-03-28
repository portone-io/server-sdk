package io.portone.sdk.server.platform.policy

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 정산 주기 계산 방식 */
@Serializable(PlatformSettlementCycleTypeSerializer::class)
public sealed interface PlatformSettlementCycleType {
  public val value: String
  /** 매일 정산 */
  @Serializable(DailySerializer::class)
  public data object Daily : PlatformSettlementCycleType {
    override val value: String = "DAILY"
  }
  private object DailySerializer : KSerializer<Daily> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Daily::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Daily = decoder.decodeString().let {
      if (it != "DAILY") {
        throw SerializationException(it)
      } else {
        return Daily
      }
    }
    override fun serialize(encoder: Encoder, value: Daily) = encoder.encodeString(value.value)
  }
  /** 매주 정해진 요일에 정산 */
  @Serializable(WeeklySerializer::class)
  public data object Weekly : PlatformSettlementCycleType {
    override val value: String = "WEEKLY"
  }
  private object WeeklySerializer : KSerializer<Weekly> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Weekly::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Weekly = decoder.decodeString().let {
      if (it != "WEEKLY") {
        throw SerializationException(it)
      } else {
        return Weekly
      }
    }
    override fun serialize(encoder: Encoder, value: Weekly) = encoder.encodeString(value.value)
  }
  /** 매월 정해진 날(일)에 정산 */
  @Serializable(MonthlySerializer::class)
  public data object Monthly : PlatformSettlementCycleType {
    override val value: String = "MONTHLY"
  }
  private object MonthlySerializer : KSerializer<Monthly> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Monthly::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Monthly = decoder.decodeString().let {
      if (it != "MONTHLY") {
        throw SerializationException(it)
      } else {
        return Monthly
      }
    }
    override fun serialize(encoder: Encoder, value: Monthly) = encoder.encodeString(value.value)
  }
  /** 정해진 날짜(월, 일)에 정산 */
  @Serializable(ManualDatesSerializer::class)
  public data object ManualDates : PlatformSettlementCycleType {
    override val value: String = "MANUAL_DATES"
  }
  private object ManualDatesSerializer : KSerializer<ManualDates> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ManualDates::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ManualDates = decoder.decodeString().let {
      if (it != "MANUAL_DATES") {
        throw SerializationException(it)
      } else {
        return ManualDates
      }
    }
    override fun serialize(encoder: Encoder, value: ManualDates) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleType
}


private object PlatformSettlementCycleTypeSerializer : KSerializer<PlatformSettlementCycleType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformSettlementCycleType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformSettlementCycleType {
    val value = decoder.decodeString()
    return when (value) {
      "DAILY" -> PlatformSettlementCycleType.Daily
      "WEEKLY" -> PlatformSettlementCycleType.Weekly
      "MONTHLY" -> PlatformSettlementCycleType.Monthly
      "MANUAL_DATES" -> PlatformSettlementCycleType.ManualDates
      else -> PlatformSettlementCycleType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformSettlementCycleType) = encoder.encodeString(value.value)
}
