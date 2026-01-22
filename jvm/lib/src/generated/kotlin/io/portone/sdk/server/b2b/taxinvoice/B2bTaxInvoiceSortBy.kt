package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 세금계산서 정렬 기준 */
@Serializable(B2bTaxInvoiceSortBySerializer::class)
public sealed interface B2bTaxInvoiceSortBy {
  public val value: String
  /** 작성일자 */
  @Serializable(WriteDateSerializer::class)
  public data object WriteDate : B2bTaxInvoiceSortBy {
    override val value: String = "WRITE_DATE"
  }
  public object WriteDateSerializer : KSerializer<WriteDate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WriteDate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WriteDate = decoder.decodeString().let {
      if (it != "WRITE_DATE") {
        throw SerializationException(it)
      } else {
        return WriteDate
      }
    }
    override fun serialize(encoder: Encoder, value: WriteDate): Unit = encoder.encodeString(value.value)
  }
  /** 발행마감일 */
  @Serializable(IssuanceDueDateSerializer::class)
  public data object IssuanceDueDate : B2bTaxInvoiceSortBy {
    override val value: String = "ISSUANCE_DUE_DATE"
  }
  public object IssuanceDueDateSerializer : KSerializer<IssuanceDueDate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuanceDueDate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuanceDueDate = decoder.decodeString().let {
      if (it != "ISSUANCE_DUE_DATE") {
        throw SerializationException(it)
      } else {
        return IssuanceDueDate
      }
    }
    override fun serialize(encoder: Encoder, value: IssuanceDueDate): Unit = encoder.encodeString(value.value)
  }
  /** 합계금액 */
  @Serializable(TotalAmountSerializer::class)
  public data object TotalAmount : B2bTaxInvoiceSortBy {
    override val value: String = "TOTAL_AMOUNT"
  }
  public object TotalAmountSerializer : KSerializer<TotalAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TotalAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TotalAmount = decoder.decodeString().let {
      if (it != "TOTAL_AMOUNT") {
        throw SerializationException(it)
      } else {
        return TotalAmount
      }
    }
    override fun serialize(encoder: Encoder, value: TotalAmount): Unit = encoder.encodeString(value.value)
  }
  /** 공급가액 */
  @Serializable(TotalSupplyAmountSerializer::class)
  public data object TotalSupplyAmount : B2bTaxInvoiceSortBy {
    override val value: String = "TOTAL_SUPPLY_AMOUNT"
  }
  public object TotalSupplyAmountSerializer : KSerializer<TotalSupplyAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TotalSupplyAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TotalSupplyAmount = decoder.decodeString().let {
      if (it != "TOTAL_SUPPLY_AMOUNT") {
        throw SerializationException(it)
      } else {
        return TotalSupplyAmount
      }
    }
    override fun serialize(encoder: Encoder, value: TotalSupplyAmount): Unit = encoder.encodeString(value.value)
  }
  /** 세액 */
  @Serializable(TotalTaxAmountSerializer::class)
  public data object TotalTaxAmount : B2bTaxInvoiceSortBy {
    override val value: String = "TOTAL_TAX_AMOUNT"
  }
  public object TotalTaxAmountSerializer : KSerializer<TotalTaxAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TotalTaxAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TotalTaxAmount = decoder.decodeString().let {
      if (it != "TOTAL_TAX_AMOUNT") {
        throw SerializationException(it)
      } else {
        return TotalTaxAmount
      }
    }
    override fun serialize(encoder: Encoder, value: TotalTaxAmount): Unit = encoder.encodeString(value.value)
  }
  /** 발행요청일시 */
  @Serializable(RequestedAtSerializer::class)
  public data object RequestedAt : B2bTaxInvoiceSortBy {
    override val value: String = "REQUESTED_AT"
  }
  public object RequestedAtSerializer : KSerializer<RequestedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RequestedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RequestedAt = decoder.decodeString().let {
      if (it != "REQUESTED_AT") {
        throw SerializationException(it)
      } else {
        return RequestedAt
      }
    }
    override fun serialize(encoder: Encoder, value: RequestedAt): Unit = encoder.encodeString(value.value)
  }
  /** 발행완료일시 */
  @Serializable(IssuedAtSerializer::class)
  public data object IssuedAt : B2bTaxInvoiceSortBy {
    override val value: String = "ISSUED_AT"
  }
  public object IssuedAtSerializer : KSerializer<IssuedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuedAt = decoder.decodeString().let {
      if (it != "ISSUED_AT") {
        throw SerializationException(it)
      } else {
        return IssuedAt
      }
    }
    override fun serialize(encoder: Encoder, value: IssuedAt): Unit = encoder.encodeString(value.value)
  }
  /** 국세청전송일시 */
  @Serializable(NtsSentAtSerializer::class)
  public data object NtsSentAt : B2bTaxInvoiceSortBy {
    override val value: String = "NTS_SENT_AT"
  }
  public object NtsSentAtSerializer : KSerializer<NtsSentAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NtsSentAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NtsSentAt = decoder.decodeString().let {
      if (it != "NTS_SENT_AT") {
        throw SerializationException(it)
      } else {
        return NtsSentAt
      }
    }
    override fun serialize(encoder: Encoder, value: NtsSentAt): Unit = encoder.encodeString(value.value)
  }
  /** 상태 업데이트 일시 */
  @Serializable(StatusUpdatedAtSerializer::class)
  public data object StatusUpdatedAt : B2bTaxInvoiceSortBy {
    override val value: String = "STATUS_UPDATED_AT"
  }
  public object StatusUpdatedAtSerializer : KSerializer<StatusUpdatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusUpdatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusUpdatedAt = decoder.decodeString().let {
      if (it != "STATUS_UPDATED_AT") {
        throw SerializationException(it)
      } else {
        return StatusUpdatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: StatusUpdatedAt): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceSortBy
}


public object B2bTaxInvoiceSortBySerializer : KSerializer<B2bTaxInvoiceSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceSortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "WRITE_DATE" -> B2bTaxInvoiceSortBy.WriteDate
      "ISSUANCE_DUE_DATE" -> B2bTaxInvoiceSortBy.IssuanceDueDate
      "TOTAL_AMOUNT" -> B2bTaxInvoiceSortBy.TotalAmount
      "TOTAL_SUPPLY_AMOUNT" -> B2bTaxInvoiceSortBy.TotalSupplyAmount
      "TOTAL_TAX_AMOUNT" -> B2bTaxInvoiceSortBy.TotalTaxAmount
      "REQUESTED_AT" -> B2bTaxInvoiceSortBy.RequestedAt
      "ISSUED_AT" -> B2bTaxInvoiceSortBy.IssuedAt
      "NTS_SENT_AT" -> B2bTaxInvoiceSortBy.NtsSentAt
      "STATUS_UPDATED_AT" -> B2bTaxInvoiceSortBy.StatusUpdatedAt
      else -> B2bTaxInvoiceSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceSortBy): Unit = encoder.encodeString(value.value)
}
