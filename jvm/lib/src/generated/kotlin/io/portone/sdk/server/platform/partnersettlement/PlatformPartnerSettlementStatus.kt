package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 상태 */
@Serializable(PlatformPartnerSettlementStatusSerializer::class)
public sealed interface PlatformPartnerSettlementStatus {
  public val value: String
  /** 지급 예약 */
  @Serializable(PayoutScheduledSerializer::class)
  public data object PayoutScheduled : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_SCHEDULED"
  }
  private object PayoutScheduledSerializer : KSerializer<PayoutScheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayoutScheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayoutScheduled = decoder.decodeString().let {
      if (it != "PAYOUT_SCHEDULED") {
        throw SerializationException(it)
      } else {
        return PayoutScheduled
      }
    }
    override fun serialize(encoder: Encoder, value: PayoutScheduled) = encoder.encodeString(value.value)
  }
  /** 지급 예정 */
  @Serializable(PayoutPreparedSerializer::class)
  public data object PayoutPrepared : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_PREPARED"
  }
  private object PayoutPreparedSerializer : KSerializer<PayoutPrepared> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayoutPrepared::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayoutPrepared = decoder.decodeString().let {
      if (it != "PAYOUT_PREPARED") {
        throw SerializationException(it)
      } else {
        return PayoutPrepared
      }
    }
    override fun serialize(encoder: Encoder, value: PayoutPrepared) = encoder.encodeString(value.value)
  }
  /** 지급 보류 */
  @Serializable(PayoutWithheldSerializer::class)
  public data object PayoutWithheld : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_WITHHELD"
  }
  private object PayoutWithheldSerializer : KSerializer<PayoutWithheld> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayoutWithheld::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayoutWithheld = decoder.decodeString().let {
      if (it != "PAYOUT_WITHHELD") {
        throw SerializationException(it)
      } else {
        return PayoutWithheld
      }
    }
    override fun serialize(encoder: Encoder, value: PayoutWithheld) = encoder.encodeString(value.value)
  }
  /** 지급 실패 */
  @Serializable(PayoutFailedSerializer::class)
  public data object PayoutFailed : PlatformPartnerSettlementStatus {
    override val value: String = "PAYOUT_FAILED"
  }
  private object PayoutFailedSerializer : KSerializer<PayoutFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayoutFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayoutFailed = decoder.decodeString().let {
      if (it != "PAYOUT_FAILED") {
        throw SerializationException(it)
      } else {
        return PayoutFailed
      }
    }
    override fun serialize(encoder: Encoder, value: PayoutFailed) = encoder.encodeString(value.value)
  }
  /** 지급 중 */
  @Serializable(InPayoutSerializer::class)
  public data object InPayout : PlatformPartnerSettlementStatus {
    override val value: String = "IN_PAYOUT"
  }
  private object InPayoutSerializer : KSerializer<InPayout> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InPayout::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InPayout = decoder.decodeString().let {
      if (it != "IN_PAYOUT") {
        throw SerializationException(it)
      } else {
        return InPayout
      }
    }
    override fun serialize(encoder: Encoder, value: InPayout) = encoder.encodeString(value.value)
  }
  /** 지급 완료 */
  @Serializable(PaidOutSerializer::class)
  public data object PaidOut : PlatformPartnerSettlementStatus {
    override val value: String = "PAID_OUT"
  }
  private object PaidOutSerializer : KSerializer<PaidOut> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaidOut::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PaidOut = decoder.decodeString().let {
      if (it != "PAID_OUT") {
        throw SerializationException(it)
      } else {
        return PaidOut
      }
    }
    override fun serialize(encoder: Encoder, value: PaidOut) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementStatus
}


private object PlatformPartnerSettlementStatusSerializer : KSerializer<PlatformPartnerSettlementStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerSettlementStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerSettlementStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PAYOUT_SCHEDULED" -> PlatformPartnerSettlementStatus.PayoutScheduled
      "PAYOUT_PREPARED" -> PlatformPartnerSettlementStatus.PayoutPrepared
      "PAYOUT_WITHHELD" -> PlatformPartnerSettlementStatus.PayoutWithheld
      "PAYOUT_FAILED" -> PlatformPartnerSettlementStatus.PayoutFailed
      "IN_PAYOUT" -> PlatformPartnerSettlementStatus.InPayout
      "PAID_OUT" -> PlatformPartnerSettlementStatus.PaidOut
      else -> PlatformPartnerSettlementStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerSettlementStatus) = encoder.encodeString(value.value)
}
