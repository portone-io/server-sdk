package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(B2bTaxInvoiceStatusSerializer::class)
public sealed interface B2bTaxInvoiceStatus {
  public val value: String
  /** 임시저장 */
  @Serializable(DraftedSerializer::class)
  public data object Drafted : B2bTaxInvoiceStatus {
    override val value: String = "DRAFTED"
  }
  public object DraftedSerializer : KSerializer<Drafted> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Drafted::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Drafted = decoder.decodeString().let {
      if (it != "DRAFTED") {
        throw SerializationException(it)
      } else {
        return Drafted
      }
    }
    override fun serialize(encoder: Encoder, value: Drafted): Unit = encoder.encodeString(value.value)
  }
  /** 임시저장 대기 */
  @Serializable(DraftPendingSerializer::class)
  public data object DraftPending : B2bTaxInvoiceStatus {
    override val value: String = "DRAFT_PENDING"
  }
  public object DraftPendingSerializer : KSerializer<DraftPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DraftPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DraftPending = decoder.decodeString().let {
      if (it != "DRAFT_PENDING") {
        throw SerializationException(it)
      } else {
        return DraftPending
      }
    }
    override fun serialize(encoder: Encoder, value: DraftPending): Unit = encoder.encodeString(value.value)
  }
  /** 임시저장 실패 */
  @Serializable(DraftFailedSerializer::class)
  public data object DraftFailed : B2bTaxInvoiceStatus {
    override val value: String = "DRAFT_FAILED"
  }
  public object DraftFailedSerializer : KSerializer<DraftFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DraftFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DraftFailed = decoder.decodeString().let {
      if (it != "DRAFT_FAILED") {
        throw SerializationException(it)
      } else {
        return DraftFailed
      }
    }
    override fun serialize(encoder: Encoder, value: DraftFailed): Unit = encoder.encodeString(value.value)
  }
  /** 역발행 요청 완료 (전자 서명 요청됨) */
  @Serializable(RequestedSerializer::class)
  public data object Requested : B2bTaxInvoiceStatus {
    override val value: String = "REQUESTED"
  }
  public object RequestedSerializer : KSerializer<Requested> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Requested::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Requested = decoder.decodeString().let {
      if (it != "REQUESTED") {
        throw SerializationException(it)
      } else {
        return Requested
      }
    }
    override fun serialize(encoder: Encoder, value: Requested): Unit = encoder.encodeString(value.value)
  }
  /** 역발행 요청 대기 */
  @Serializable(RequestPendingSerializer::class)
  public data object RequestPending : B2bTaxInvoiceStatus {
    override val value: String = "REQUEST_PENDING"
  }
  public object RequestPendingSerializer : KSerializer<RequestPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestPending = decoder.decodeString().let {
      if (it != "REQUEST_PENDING") {
        throw SerializationException(it)
      } else {
        return RequestPending
      }
    }
    override fun serialize(encoder: Encoder, value: RequestPending): Unit = encoder.encodeString(value.value)
  }
  /** 역발행 요청 실패 */
  @Serializable(RequestFailedSerializer::class)
  public data object RequestFailed : B2bTaxInvoiceStatus {
    override val value: String = "REQUEST_FAILED"
  }
  public object RequestFailedSerializer : KSerializer<RequestFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestFailed = decoder.decodeString().let {
      if (it != "REQUEST_FAILED") {
        throw SerializationException(it)
      } else {
        return RequestFailed
      }
    }
    override fun serialize(encoder: Encoder, value: RequestFailed): Unit = encoder.encodeString(value.value)
  }
  /** 공급받는자에 의한 발행취소 */
  @Serializable(RequestCancelledSerializer::class)
  public data object RequestCancelled : B2bTaxInvoiceStatus {
    override val value: String = "REQUEST_CANCELLED"
  }
  public object RequestCancelledSerializer : KSerializer<RequestCancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestCancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestCancelled = decoder.decodeString().let {
      if (it != "REQUEST_CANCELLED") {
        throw SerializationException(it)
      } else {
        return RequestCancelled
      }
    }
    override fun serialize(encoder: Encoder, value: RequestCancelled): Unit = encoder.encodeString(value.value)
  }
  /** 발행완료 */
  @Serializable(IssuedSerializer::class)
  public data object Issued : B2bTaxInvoiceStatus {
    override val value: String = "ISSUED"
  }
  public object IssuedSerializer : KSerializer<Issued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Issued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Issued = decoder.decodeString().let {
      if (it != "ISSUED") {
        throw SerializationException(it)
      } else {
        return Issued
      }
    }
    override fun serialize(encoder: Encoder, value: Issued): Unit = encoder.encodeString(value.value)
  }
  /** 발행 대기 */
  @Serializable(IssuePendingSerializer::class)
  public data object IssuePending : B2bTaxInvoiceStatus {
    override val value: String = "ISSUE_PENDING"
  }
  public object IssuePendingSerializer : KSerializer<IssuePending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuePending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuePending = decoder.decodeString().let {
      if (it != "ISSUE_PENDING") {
        throw SerializationException(it)
      } else {
        return IssuePending
      }
    }
    override fun serialize(encoder: Encoder, value: IssuePending): Unit = encoder.encodeString(value.value)
  }
  /** 발행 실패 */
  @Serializable(IssueFailedSerializer::class)
  public data object IssueFailed : B2bTaxInvoiceStatus {
    override val value: String = "ISSUE_FAILED"
  }
  public object IssueFailedSerializer : KSerializer<IssueFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssueFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssueFailed = decoder.decodeString().let {
      if (it != "ISSUE_FAILED") {
        throw SerializationException(it)
      } else {
        return IssueFailed
      }
    }
    override fun serialize(encoder: Encoder, value: IssueFailed): Unit = encoder.encodeString(value.value)
  }
  /** 전송전 */
  @Serializable(BeforeSendingSerializer::class)
  public data object BeforeSending : B2bTaxInvoiceStatus {
    override val value: String = "BEFORE_SENDING"
  }
  public object BeforeSendingSerializer : KSerializer<BeforeSending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BeforeSending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BeforeSending = decoder.decodeString().let {
      if (it != "BEFORE_SENDING") {
        throw SerializationException(it)
      } else {
        return BeforeSending
      }
    }
    override fun serialize(encoder: Encoder, value: BeforeSending): Unit = encoder.encodeString(value.value)
  }
  /** 전송대기 */
  @Serializable(WaitingSendingSerializer::class)
  public data object WaitingSending : B2bTaxInvoiceStatus {
    override val value: String = "WAITING_SENDING"
  }
  public object WaitingSendingSerializer : KSerializer<WaitingSending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WaitingSending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WaitingSending = decoder.decodeString().let {
      if (it != "WAITING_SENDING") {
        throw SerializationException(it)
      } else {
        return WaitingSending
      }
    }
    override fun serialize(encoder: Encoder, value: WaitingSending): Unit = encoder.encodeString(value.value)
  }
  /** 전송중 */
  @Serializable(SendingSerializer::class)
  public data object Sending : B2bTaxInvoiceStatus {
    override val value: String = "SENDING"
  }
  public object SendingSerializer : KSerializer<Sending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sending = decoder.decodeString().let {
      if (it != "SENDING") {
        throw SerializationException(it)
      } else {
        return Sending
      }
    }
    override fun serialize(encoder: Encoder, value: Sending): Unit = encoder.encodeString(value.value)
  }
  /** 전송완료 */
  @Serializable(SendingCompletedSerializer::class)
  public data object SendingCompleted : B2bTaxInvoiceStatus {
    override val value: String = "SENDING_COMPLETED"
  }
  public object SendingCompletedSerializer : KSerializer<SendingCompleted> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SendingCompleted::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SendingCompleted = decoder.decodeString().let {
      if (it != "SENDING_COMPLETED") {
        throw SerializationException(it)
      } else {
        return SendingCompleted
      }
    }
    override fun serialize(encoder: Encoder, value: SendingCompleted): Unit = encoder.encodeString(value.value)
  }
  /** 전송실패 */
  @Serializable(SendingFailedSerializer::class)
  public data object SendingFailed : B2bTaxInvoiceStatus {
    override val value: String = "SENDING_FAILED"
  }
  public object SendingFailedSerializer : KSerializer<SendingFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SendingFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SendingFailed = decoder.decodeString().let {
      if (it != "SENDING_FAILED") {
        throw SerializationException(it)
      } else {
        return SendingFailed
      }
    }
    override fun serialize(encoder: Encoder, value: SendingFailed): Unit = encoder.encodeString(value.value)
  }
  /** 공급자의 발행거부 */
  @Serializable(RequestRefusedSerializer::class)
  public data object RequestRefused : B2bTaxInvoiceStatus {
    override val value: String = "REQUEST_REFUSED"
  }
  public object RequestRefusedSerializer : KSerializer<RequestRefused> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestRefused::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestRefused = decoder.decodeString().let {
      if (it != "REQUEST_REFUSED") {
        throw SerializationException(it)
      } else {
        return RequestRefused
      }
    }
    override fun serialize(encoder: Encoder, value: RequestRefused): Unit = encoder.encodeString(value.value)
  }
  /** 공급자에 의한 발행 취소 */
  @Serializable(IssuanceCancelledSerializer::class)
  public data object IssuanceCancelled : B2bTaxInvoiceStatus {
    override val value: String = "ISSUANCE_CANCELLED"
  }
  public object IssuanceCancelledSerializer : KSerializer<IssuanceCancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuanceCancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuanceCancelled = decoder.decodeString().let {
      if (it != "ISSUANCE_CANCELLED") {
        throw SerializationException(it)
      } else {
        return IssuanceCancelled
      }
    }
    override fun serialize(encoder: Encoder, value: IssuanceCancelled): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceStatus
}


public object B2bTaxInvoiceStatusSerializer : KSerializer<B2bTaxInvoiceStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceStatus {
    val value = decoder.decodeString()
    return when (value) {
      "DRAFTED" -> B2bTaxInvoiceStatus.Drafted
      "DRAFT_PENDING" -> B2bTaxInvoiceStatus.DraftPending
      "DRAFT_FAILED" -> B2bTaxInvoiceStatus.DraftFailed
      "REQUESTED" -> B2bTaxInvoiceStatus.Requested
      "REQUEST_PENDING" -> B2bTaxInvoiceStatus.RequestPending
      "REQUEST_FAILED" -> B2bTaxInvoiceStatus.RequestFailed
      "REQUEST_CANCELLED" -> B2bTaxInvoiceStatus.RequestCancelled
      "ISSUED" -> B2bTaxInvoiceStatus.Issued
      "ISSUE_PENDING" -> B2bTaxInvoiceStatus.IssuePending
      "ISSUE_FAILED" -> B2bTaxInvoiceStatus.IssueFailed
      "BEFORE_SENDING" -> B2bTaxInvoiceStatus.BeforeSending
      "WAITING_SENDING" -> B2bTaxInvoiceStatus.WaitingSending
      "SENDING" -> B2bTaxInvoiceStatus.Sending
      "SENDING_COMPLETED" -> B2bTaxInvoiceStatus.SendingCompleted
      "SENDING_FAILED" -> B2bTaxInvoiceStatus.SendingFailed
      "REQUEST_REFUSED" -> B2bTaxInvoiceStatus.RequestRefused
      "ISSUANCE_CANCELLED" -> B2bTaxInvoiceStatus.IssuanceCancelled
      else -> B2bTaxInvoiceStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceStatus): Unit = encoder.encodeString(value.value)
}
