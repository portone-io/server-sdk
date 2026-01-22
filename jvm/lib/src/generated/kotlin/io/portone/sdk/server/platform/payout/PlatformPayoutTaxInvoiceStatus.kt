package io.portone.sdk.server.platform.payout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformPayoutTaxInvoiceStatusSerializer::class)
public sealed interface PlatformPayoutTaxInvoiceStatus {
  public val value: String
  @Serializable(NoneSerializer::class)
  public data object None : PlatformPayoutTaxInvoiceStatus {
    override val value: String = "NONE"
  }
  public object NoneSerializer : KSerializer<None> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(None::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): None = decoder.decodeString().let {
      if (it != "NONE") {
        throw SerializationException(it)
      } else {
        return None
      }
    }
    override fun serialize(encoder: Encoder, value: None): Unit = encoder.encodeString(value.value)
  }
  @Serializable(DraftedSerializer::class)
  public data object Drafted : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(DraftPendingSerializer::class)
  public data object DraftPending : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(DraftFailedSerializer::class)
  public data object DraftFailed : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(RequestedSerializer::class)
  public data object Requested : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(RequestPendingSerializer::class)
  public data object RequestPending : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(RequestFailedSerializer::class)
  public data object RequestFailed : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(RequestCancelledSerializer::class)
  public data object RequestCancelled : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(RequestRefusedSerializer::class)
  public data object RequestRefused : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(IssuedSerializer::class)
  public data object Issued : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(IssuanceCancelledSerializer::class)
  public data object IssuanceCancelled : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(BeforeSendingSerializer::class)
  public data object BeforeSending : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(WaitingSendingSerializer::class)
  public data object WaitingSending : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(SendingSerializer::class)
  public data object Sending : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(SendingCompletedSerializer::class)
  public data object SendingCompleted : PlatformPayoutTaxInvoiceStatus {
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
  @Serializable(SendingFailedSerializer::class)
  public data object SendingFailed : PlatformPayoutTaxInvoiceStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutTaxInvoiceStatus
}


public object PlatformPayoutTaxInvoiceStatusSerializer : KSerializer<PlatformPayoutTaxInvoiceStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutTaxInvoiceStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutTaxInvoiceStatus {
    val value = decoder.decodeString()
    return when (value) {
      "NONE" -> PlatformPayoutTaxInvoiceStatus.None
      "DRAFTED" -> PlatformPayoutTaxInvoiceStatus.Drafted
      "DRAFT_PENDING" -> PlatformPayoutTaxInvoiceStatus.DraftPending
      "DRAFT_FAILED" -> PlatformPayoutTaxInvoiceStatus.DraftFailed
      "REQUESTED" -> PlatformPayoutTaxInvoiceStatus.Requested
      "REQUEST_PENDING" -> PlatformPayoutTaxInvoiceStatus.RequestPending
      "REQUEST_FAILED" -> PlatformPayoutTaxInvoiceStatus.RequestFailed
      "REQUEST_CANCELLED" -> PlatformPayoutTaxInvoiceStatus.RequestCancelled
      "REQUEST_REFUSED" -> PlatformPayoutTaxInvoiceStatus.RequestRefused
      "ISSUED" -> PlatformPayoutTaxInvoiceStatus.Issued
      "ISSUANCE_CANCELLED" -> PlatformPayoutTaxInvoiceStatus.IssuanceCancelled
      "BEFORE_SENDING" -> PlatformPayoutTaxInvoiceStatus.BeforeSending
      "WAITING_SENDING" -> PlatformPayoutTaxInvoiceStatus.WaitingSending
      "SENDING" -> PlatformPayoutTaxInvoiceStatus.Sending
      "SENDING_COMPLETED" -> PlatformPayoutTaxInvoiceStatus.SendingCompleted
      "SENDING_FAILED" -> PlatformPayoutTaxInvoiceStatus.SendingFailed
      else -> PlatformPayoutTaxInvoiceStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutTaxInvoiceStatus): Unit = encoder.encodeString(value.value)
}
