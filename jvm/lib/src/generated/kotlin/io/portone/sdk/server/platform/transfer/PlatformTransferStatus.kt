package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 상태 */
@Serializable(PlatformTransferStatusSerializer::class)
public sealed interface PlatformTransferStatus {
  public val value: String
  /** 정산 예약 */
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PlatformTransferStatus {
    override val value: String = "SCHEDULED"
  }
  public object ScheduledSerializer : KSerializer<Scheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scheduled = decoder.decodeString().let {
      if (it != "SCHEDULED") {
        throw SerializationException(it)
      } else {
        return Scheduled
      }
    }
    override fun serialize(encoder: Encoder, value: Scheduled): Unit = encoder.encodeString(value.value)
  }
  /** 정산 중 */
  @Serializable(InProcessSerializer::class)
  public data object InProcess : PlatformTransferStatus {
    override val value: String = "IN_PROCESS"
  }
  public object InProcessSerializer : KSerializer<InProcess> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InProcess::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InProcess = decoder.decodeString().let {
      if (it != "IN_PROCESS") {
        throw SerializationException(it)
      } else {
        return InProcess
      }
    }
    override fun serialize(encoder: Encoder, value: InProcess): Unit = encoder.encodeString(value.value)
  }
  /** 정산 완료 */
  @Serializable(SettledSerializer::class)
  public data object Settled : PlatformTransferStatus {
    override val value: String = "SETTLED"
  }
  public object SettledSerializer : KSerializer<Settled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Settled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Settled = decoder.decodeString().let {
      if (it != "SETTLED") {
        throw SerializationException(it)
      } else {
        return Settled
      }
    }
    override fun serialize(encoder: Encoder, value: Settled): Unit = encoder.encodeString(value.value)
  }
  /** 지급 중 */
  @Serializable(InPayoutSerializer::class)
  public data object InPayout : PlatformTransferStatus {
    override val value: String = "IN_PAYOUT"
  }
  public object InPayoutSerializer : KSerializer<InPayout> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InPayout::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InPayout = decoder.decodeString().let {
      if (it != "IN_PAYOUT") {
        throw SerializationException(it)
      } else {
        return InPayout
      }
    }
    override fun serialize(encoder: Encoder, value: InPayout): Unit = encoder.encodeString(value.value)
  }
  /** 지급 완료 */
  @Serializable(PaidOutSerializer::class)
  public data object PaidOut : PlatformTransferStatus {
    override val value: String = "PAID_OUT"
  }
  public object PaidOutSerializer : KSerializer<PaidOut> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaidOut::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PaidOut = decoder.decodeString().let {
      if (it != "PAID_OUT") {
        throw SerializationException(it)
      } else {
        return PaidOut
      }
    }
    override fun serialize(encoder: Encoder, value: PaidOut): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferStatus
}


public object PlatformTransferStatusSerializer : KSerializer<PlatformTransferStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PlatformTransferStatus.Scheduled
      "IN_PROCESS" -> PlatformTransferStatus.InProcess
      "SETTLED" -> PlatformTransferStatus.Settled
      "IN_PAYOUT" -> PlatformTransferStatus.InPayout
      "PAID_OUT" -> PlatformTransferStatus.PaidOut
      else -> PlatformTransferStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferStatus): Unit = encoder.encodeString(value.value)
}
