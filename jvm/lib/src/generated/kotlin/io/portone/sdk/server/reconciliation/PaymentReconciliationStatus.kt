package io.portone.sdk.server.reconciliation

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 건의 대사 상태 */
@Serializable(PaymentReconciliationStatusSerializer::class)
public sealed interface PaymentReconciliationStatus {
  public val value: String
  /** 대사 매칭 성공 상태 */
  @Serializable(MatchedSerializer::class)
  public data object Matched : PaymentReconciliationStatus {
    override val value: String = "MATCHED"
  }
  private object MatchedSerializer : KSerializer<Matched> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Matched::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Matched = decoder.decodeString().let {
      if (it != "MATCHED") {
        throw SerializationException(it)
      } else {
        return Matched
      }
    }
    override fun serialize(encoder: Encoder, value: Matched) = encoder.encodeString(value.value)
  }
  /** 대사 매칭 실패 상태 */
  @Serializable(NotMatchedSerializer::class)
  public data object NotMatched : PaymentReconciliationStatus {
    override val value: String = "NOT_MATCHED"
  }
  private object NotMatchedSerializer : KSerializer<NotMatched> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotMatched::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotMatched = decoder.decodeString().let {
      if (it != "NOT_MATCHED") {
        throw SerializationException(it)
      } else {
        return NotMatched
      }
    }
    override fun serialize(encoder: Encoder, value: NotMatched) = encoder.encodeString(value.value)
  }
  /** 대사 불가능 상태 */
  @Serializable(IncomparableSerializer::class)
  public data object Incomparable : PaymentReconciliationStatus {
    override val value: String = "INCOMPARABLE"
  }
  private object IncomparableSerializer : KSerializer<Incomparable> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Incomparable::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Incomparable = decoder.decodeString().let {
      if (it != "INCOMPARABLE") {
        throw SerializationException(it)
      } else {
        return Incomparable
      }
    }
    override fun serialize(encoder: Encoder, value: Incomparable) = encoder.encodeString(value.value)
  }
  /** PG사 결제 정보가 수집되지 않은 상태 */
  @Serializable(NotCollectedSerializer::class)
  public data object NotCollected : PaymentReconciliationStatus {
    override val value: String = "NOT_COLLECTED"
  }
  private object NotCollectedSerializer : KSerializer<NotCollected> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotCollected::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotCollected = decoder.decodeString().let {
      if (it != "NOT_COLLECTED") {
        throw SerializationException(it)
      } else {
        return NotCollected
      }
    }
    override fun serialize(encoder: Encoder, value: NotCollected) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentReconciliationStatus
}


private object PaymentReconciliationStatusSerializer : KSerializer<PaymentReconciliationStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentReconciliationStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentReconciliationStatus {
    val value = decoder.decodeString()
    return when (value) {
      "MATCHED" -> PaymentReconciliationStatus.Matched
      "NOT_MATCHED" -> PaymentReconciliationStatus.NotMatched
      "INCOMPARABLE" -> PaymentReconciliationStatus.Incomparable
      "NOT_COLLECTED" -> PaymentReconciliationStatus.NotCollected
      else -> PaymentReconciliationStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentReconciliationStatus) = encoder.encodeString(value.value)
}
