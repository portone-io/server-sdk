package io.portone.sdk.server.b2b.counterparty

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 거래처 휴폐업 상태 */
@Serializable(B2bCounterpartyBusinessStatusSerializer::class)
public sealed interface B2bCounterpartyBusinessStatus {
  public val value: String
  /** 미조회 */
  @Serializable(UnknownSerializer::class)
  public data object Unknown : B2bCounterpartyBusinessStatus {
    override val value: String = "UNKNOWN"
  }
  public object UnknownSerializer : KSerializer<Unknown> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unknown::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unknown = decoder.decodeString().let {
      if (it != "UNKNOWN") {
        throw SerializationException(it)
      } else {
        return Unknown
      }
    }
    override fun serialize(encoder: Encoder, value: Unknown): Unit = encoder.encodeString(value.value)
  }
  /** 영업중 */
  @Serializable(InBusinessSerializer::class)
  public data object InBusiness : B2bCounterpartyBusinessStatus {
    override val value: String = "IN_BUSINESS"
  }
  public object InBusinessSerializer : KSerializer<InBusiness> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InBusiness::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): InBusiness = decoder.decodeString().let {
      if (it != "IN_BUSINESS") {
        throw SerializationException(it)
      } else {
        return InBusiness
      }
    }
    override fun serialize(encoder: Encoder, value: InBusiness): Unit = encoder.encodeString(value.value)
  }
  /** 폐업 */
  @Serializable(ClosedSerializer::class)
  public data object Closed : B2bCounterpartyBusinessStatus {
    override val value: String = "CLOSED"
  }
  public object ClosedSerializer : KSerializer<Closed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Closed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Closed = decoder.decodeString().let {
      if (it != "CLOSED") {
        throw SerializationException(it)
      } else {
        return Closed
      }
    }
    override fun serialize(encoder: Encoder, value: Closed): Unit = encoder.encodeString(value.value)
  }
  /** 휴업 */
  @Serializable(SuspendedSerializer::class)
  public data object Suspended : B2bCounterpartyBusinessStatus {
    override val value: String = "SUSPENDED"
  }
  public object SuspendedSerializer : KSerializer<Suspended> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Suspended::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Suspended = decoder.decodeString().let {
      if (it != "SUSPENDED") {
        throw SerializationException(it)
      } else {
        return Suspended
      }
    }
    override fun serialize(encoder: Encoder, value: Suspended): Unit = encoder.encodeString(value.value)
  }
  /** 사업체 미등록 */
  @Serializable(NotFoundSerializer::class)
  public data object NotFound : B2bCounterpartyBusinessStatus {
    override val value: String = "NOT_FOUND"
  }
  public object NotFoundSerializer : KSerializer<NotFound> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotFound::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotFound = decoder.decodeString().let {
      if (it != "NOT_FOUND") {
        throw SerializationException(it)
      } else {
        return NotFound
      }
    }
    override fun serialize(encoder: Encoder, value: NotFound): Unit = encoder.encodeString(value.value)
  }
  /**
   * 조회 대기
   *
   * 일괄 등록 시 조회 대기 상태입니다.
   */
  @Serializable(CheckPendingSerializer::class)
  public data object CheckPending : B2bCounterpartyBusinessStatus {
    override val value: String = "CHECK_PENDING"
  }
  public object CheckPendingSerializer : KSerializer<CheckPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CheckPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CheckPending = decoder.decodeString().let {
      if (it != "CHECK_PENDING") {
        throw SerializationException(it)
      } else {
        return CheckPending
      }
    }
    override fun serialize(encoder: Encoder, value: CheckPending): Unit = encoder.encodeString(value.value)
  }
  /** 조회 실패 */
  @Serializable(CheckFailedSerializer::class)
  public data object CheckFailed : B2bCounterpartyBusinessStatus {
    override val value: String = "CHECK_FAILED"
  }
  public object CheckFailedSerializer : KSerializer<CheckFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CheckFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CheckFailed = decoder.decodeString().let {
      if (it != "CHECK_FAILED") {
        throw SerializationException(it)
      } else {
        return CheckFailed
      }
    }
    override fun serialize(encoder: Encoder, value: CheckFailed): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bCounterpartyBusinessStatus
}


public object B2bCounterpartyBusinessStatusSerializer : KSerializer<B2bCounterpartyBusinessStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bCounterpartyBusinessStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bCounterpartyBusinessStatus {
    val value = decoder.decodeString()
    return when (value) {
      "UNKNOWN" -> B2bCounterpartyBusinessStatus.Unknown
      "IN_BUSINESS" -> B2bCounterpartyBusinessStatus.InBusiness
      "CLOSED" -> B2bCounterpartyBusinessStatus.Closed
      "SUSPENDED" -> B2bCounterpartyBusinessStatus.Suspended
      "NOT_FOUND" -> B2bCounterpartyBusinessStatus.NotFound
      "CHECK_PENDING" -> B2bCounterpartyBusinessStatus.CheckPending
      "CHECK_FAILED" -> B2bCounterpartyBusinessStatus.CheckFailed
      else -> B2bCounterpartyBusinessStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bCounterpartyBusinessStatus): Unit = encoder.encodeString(value.value)
}
