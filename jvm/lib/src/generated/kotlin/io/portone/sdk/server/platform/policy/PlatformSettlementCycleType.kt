package io.portone.sdk.server.platform.policy

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Daily : PlatformSettlementCycleType {
    override val value: String = "DAILY"
  }
  /** 매주 정해진 요일에 정산 */
  public data object Weekly : PlatformSettlementCycleType {
    override val value: String = "WEEKLY"
  }
  /** 매월 정해진 날(일)에 정산 */
  public data object Monthly : PlatformSettlementCycleType {
    override val value: String = "MONTHLY"
  }
  /** 정해진 날짜(월, 일)에 정산 */
  public data object ManualDates : PlatformSettlementCycleType {
    override val value: String = "MANUAL_DATES"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleType
}


private object PlatformSettlementCycleTypeSerializer : KSerializer<PlatformSettlementCycleType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformSettlementCycleType::class.java.canonicalName, PrimitiveKind.STRING)
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
