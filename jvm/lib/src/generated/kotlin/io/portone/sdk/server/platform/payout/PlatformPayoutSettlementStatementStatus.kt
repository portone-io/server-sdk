package io.portone.sdk.server.platform.payout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 내역서 발송 상태 */
@Serializable(PlatformPayoutSettlementStatementStatusSerializer::class)
public sealed interface PlatformPayoutSettlementStatementStatus {
  public val value: String
  /** 미발송 */
  @Serializable(UnsentSerializer::class)
  public data object Unsent : PlatformPayoutSettlementStatementStatus {
    override val value: String = "UNSENT"
  }
  private object UnsentSerializer : KSerializer<Unsent> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unsent::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unsent = decoder.decodeString().let {
      if (it != "UNSENT") {
        throw SerializationException(it)
      } else {
        return Unsent
      }
    }
    override fun serialize(encoder: Encoder, value: Unsent) = encoder.encodeString(value.value)
  }
  /** 발송 성공 */
  @Serializable(SentSerializer::class)
  public data object Sent : PlatformPayoutSettlementStatementStatus {
    override val value: String = "SENT"
  }
  private object SentSerializer : KSerializer<Sent> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sent::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sent = decoder.decodeString().let {
      if (it != "SENT") {
        throw SerializationException(it)
      } else {
        return Sent
      }
    }
    override fun serialize(encoder: Encoder, value: Sent) = encoder.encodeString(value.value)
  }
  /** 발송 실패 */
  @Serializable(SendFailedSerializer::class)
  public data object SendFailed : PlatformPayoutSettlementStatementStatus {
    override val value: String = "SEND_FAILED"
  }
  private object SendFailedSerializer : KSerializer<SendFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SendFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SendFailed = decoder.decodeString().let {
      if (it != "SEND_FAILED") {
        throw SerializationException(it)
      } else {
        return SendFailed
      }
    }
    override fun serialize(encoder: Encoder, value: SendFailed) = encoder.encodeString(value.value)
  }
  /** 발송 대기 */
  @Serializable(SendPreparedSerializer::class)
  public data object SendPrepared : PlatformPayoutSettlementStatementStatus {
    override val value: String = "SEND_PREPARED"
  }
  private object SendPreparedSerializer : KSerializer<SendPrepared> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SendPrepared::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SendPrepared = decoder.decodeString().let {
      if (it != "SEND_PREPARED") {
        throw SerializationException(it)
      } else {
        return SendPrepared
      }
    }
    override fun serialize(encoder: Encoder, value: SendPrepared) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutSettlementStatementStatus
}


private object PlatformPayoutSettlementStatementStatusSerializer : KSerializer<PlatformPayoutSettlementStatementStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutSettlementStatementStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutSettlementStatementStatus {
    val value = decoder.decodeString()
    return when (value) {
      "UNSENT" -> PlatformPayoutSettlementStatementStatus.Unsent
      "SENT" -> PlatformPayoutSettlementStatementStatus.Sent
      "SEND_FAILED" -> PlatformPayoutSettlementStatementStatus.SendFailed
      "SEND_PREPARED" -> PlatformPayoutSettlementStatementStatus.SendPrepared
      else -> PlatformPayoutSettlementStatementStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutSettlementStatementStatus) = encoder.encodeString(value.value)
}
