package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 일괄 세금계산서 상태 */
@Serializable(B2bBulkTaxInvoiceStatusSerializer::class)
public sealed interface B2bBulkTaxInvoiceStatus {
  public val value: String
  @Serializable(DraftPendingSerializer::class)
  public data object DraftPending : B2bBulkTaxInvoiceStatus {
    override val value: String = "DRAFT_PENDING"
  }
  private object DraftPendingSerializer : KSerializer<DraftPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DraftPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DraftPending = decoder.decodeString().let {
      if (it != "DRAFT_PENDING") {
        throw SerializationException(it)
      } else {
        return DraftPending
      }
    }
    override fun serialize(encoder: Encoder, value: DraftPending) = encoder.encodeString(value.value)
  }
  @Serializable(DraftedSerializer::class)
  public data object Drafted : B2bBulkTaxInvoiceStatus {
    override val value: String = "DRAFTED"
  }
  private object DraftedSerializer : KSerializer<Drafted> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Drafted::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Drafted = decoder.decodeString().let {
      if (it != "DRAFTED") {
        throw SerializationException(it)
      } else {
        return Drafted
      }
    }
    override fun serialize(encoder: Encoder, value: Drafted) = encoder.encodeString(value.value)
  }
  @Serializable(RequestPendingSerializer::class)
  public data object RequestPending : B2bBulkTaxInvoiceStatus {
    override val value: String = "REQUEST_PENDING"
  }
  private object RequestPendingSerializer : KSerializer<RequestPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestPending = decoder.decodeString().let {
      if (it != "REQUEST_PENDING") {
        throw SerializationException(it)
      } else {
        return RequestPending
      }
    }
    override fun serialize(encoder: Encoder, value: RequestPending) = encoder.encodeString(value.value)
  }
  @Serializable(IssuePendingSerializer::class)
  public data object IssuePending : B2bBulkTaxInvoiceStatus {
    override val value: String = "ISSUE_PENDING"
  }
  private object IssuePendingSerializer : KSerializer<IssuePending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuePending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuePending = decoder.decodeString().let {
      if (it != "ISSUE_PENDING") {
        throw SerializationException(it)
      } else {
        return IssuePending
      }
    }
    override fun serialize(encoder: Encoder, value: IssuePending) = encoder.encodeString(value.value)
  }
  @Serializable(InProgressSerializer::class)
  public data object InProgress : B2bBulkTaxInvoiceStatus {
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
  @Serializable(CompletedSerializer::class)
  public data object Completed : B2bBulkTaxInvoiceStatus {
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
  @Serializable(FailedSerializer::class)
  public data object Failed : B2bBulkTaxInvoiceStatus {
    override val value: String = "FAILED"
  }
  private object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed) = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : B2bBulkTaxInvoiceStatus {
    override val value: String = "CANCELLED"
  }
  private object CancelledSerializer : KSerializer<Cancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cancelled = decoder.decodeString().let {
      if (it != "CANCELLED") {
        throw SerializationException(it)
      } else {
        return Cancelled
      }
    }
    override fun serialize(encoder: Encoder, value: Cancelled) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bBulkTaxInvoiceStatus
}


private object B2bBulkTaxInvoiceStatusSerializer : KSerializer<B2bBulkTaxInvoiceStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bBulkTaxInvoiceStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bBulkTaxInvoiceStatus {
    val value = decoder.decodeString()
    return when (value) {
      "DRAFT_PENDING" -> B2bBulkTaxInvoiceStatus.DraftPending
      "DRAFTED" -> B2bBulkTaxInvoiceStatus.Drafted
      "REQUEST_PENDING" -> B2bBulkTaxInvoiceStatus.RequestPending
      "ISSUE_PENDING" -> B2bBulkTaxInvoiceStatus.IssuePending
      "IN_PROGRESS" -> B2bBulkTaxInvoiceStatus.InProgress
      "COMPLETED" -> B2bBulkTaxInvoiceStatus.Completed
      "FAILED" -> B2bBulkTaxInvoiceStatus.Failed
      "CANCELLED" -> B2bBulkTaxInvoiceStatus.Cancelled
      else -> B2bBulkTaxInvoiceStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bBulkTaxInvoiceStatus) = encoder.encodeString(value.value)
}
