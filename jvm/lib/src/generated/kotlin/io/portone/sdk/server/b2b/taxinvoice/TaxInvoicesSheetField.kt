package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 다운로드 할 시트 컬럼 */
@Serializable(TaxInvoicesSheetFieldSerializer::class)
public sealed interface TaxInvoicesSheetField {
  public val value: String
  /** 상태 */
  @Serializable(StatusSerializer::class)
  public data object Status : TaxInvoicesSheetField {
    override val value: String = "STATUS"
  }
  public object StatusSerializer : KSerializer<Status> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Status::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Status = decoder.decodeString().let {
      if (it != "STATUS") {
        throw SerializationException(it)
      } else {
        return Status
      }
    }
    override fun serialize(encoder: Encoder, value: Status): Unit = encoder.encodeString(value.value)
  }
  /** 취소사유 */
  @Serializable(CancelReasonSerializer::class)
  public data object CancelReason : TaxInvoicesSheetField {
    override val value: String = "CANCEL_REASON"
  }
  public object CancelReasonSerializer : KSerializer<CancelReason> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelReason::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CancelReason = decoder.decodeString().let {
      if (it != "CANCEL_REASON") {
        throw SerializationException(it)
      } else {
        return CancelReason
      }
    }
    override fun serialize(encoder: Encoder, value: CancelReason): Unit = encoder.encodeString(value.value)
  }
  /** 발행유형 */
  @Serializable(IssuanceTypeSerializer::class)
  public data object IssuanceType : TaxInvoicesSheetField {
    override val value: String = "ISSUANCE_TYPE"
  }
  public object IssuanceTypeSerializer : KSerializer<IssuanceType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuanceType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuanceType = decoder.decodeString().let {
      if (it != "ISSUANCE_TYPE") {
        throw SerializationException(it)
      } else {
        return IssuanceType
      }
    }
    override fun serialize(encoder: Encoder, value: IssuanceType): Unit = encoder.encodeString(value.value)
  }
  /** 문서형태 */
  @Serializable(DocumentModificationTypeSerializer::class)
  public data object DocumentModificationType : TaxInvoicesSheetField {
    override val value: String = "DOCUMENT_MODIFICATION_TYPE"
  }
  public object DocumentModificationTypeSerializer : KSerializer<DocumentModificationType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DocumentModificationType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DocumentModificationType = decoder.decodeString().let {
      if (it != "DOCUMENT_MODIFICATION_TYPE") {
        throw SerializationException(it)
      } else {
        return DocumentModificationType
      }
    }
    override fun serialize(encoder: Encoder, value: DocumentModificationType): Unit = encoder.encodeString(value.value)
  }
  /** 지연발행 */
  @Serializable(IsDelayedSerializer::class)
  public data object IsDelayed : TaxInvoicesSheetField {
    override val value: String = "IS_DELAYED"
  }
  public object IsDelayedSerializer : KSerializer<IsDelayed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IsDelayed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IsDelayed = decoder.decodeString().let {
      if (it != "IS_DELAYED") {
        throw SerializationException(it)
      } else {
        return IsDelayed
      }
    }
    override fun serialize(encoder: Encoder, value: IsDelayed): Unit = encoder.encodeString(value.value)
  }
  /** 작성일자 */
  @Serializable(WriteDateSerializer::class)
  public data object WriteDate : TaxInvoicesSheetField {
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
  public data object IssuanceDueDate : TaxInvoicesSheetField {
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
  /** 과세형태 */
  @Serializable(TaxationTypeSerializer::class)
  public data object TaxationType : TaxInvoicesSheetField {
    override val value: String = "TAXATION_TYPE"
  }
  public object TaxationTypeSerializer : KSerializer<TaxationType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TaxationType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TaxationType = decoder.decodeString().let {
      if (it != "TAXATION_TYPE") {
        throw SerializationException(it)
      } else {
        return TaxationType
      }
    }
    override fun serialize(encoder: Encoder, value: TaxationType): Unit = encoder.encodeString(value.value)
  }
  /** 영수/청구 */
  @Serializable(PurposeTypeSerializer::class)
  public data object PurposeType : TaxInvoicesSheetField {
    override val value: String = "PURPOSE_TYPE"
  }
  public object PurposeTypeSerializer : KSerializer<PurposeType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PurposeType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PurposeType = decoder.decodeString().let {
      if (it != "PURPOSE_TYPE") {
        throw SerializationException(it)
      } else {
        return PurposeType
      }
    }
    override fun serialize(encoder: Encoder, value: PurposeType): Unit = encoder.encodeString(value.value)
  }
  /** 거래처 회사명 */
  @Serializable(PartnerNameSerializer::class)
  public data object PartnerName : TaxInvoicesSheetField {
    override val value: String = "PARTNER_NAME"
  }
  public object PartnerNameSerializer : KSerializer<PartnerName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerName = decoder.decodeString().let {
      if (it != "PARTNER_NAME") {
        throw SerializationException(it)
      } else {
        return PartnerName
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerName): Unit = encoder.encodeString(value.value)
  }
  /** 거래처 사업자등록번호 */
  @Serializable(PartnerBrnSerializer::class)
  public data object PartnerBrn : TaxInvoicesSheetField {
    override val value: String = "PARTNER_BRN"
  }
  public object PartnerBrnSerializer : KSerializer<PartnerBrn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerBrn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerBrn = decoder.decodeString().let {
      if (it != "PARTNER_BRN") {
        throw SerializationException(it)
      } else {
        return PartnerBrn
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerBrn): Unit = encoder.encodeString(value.value)
  }
  /** 합계금액 */
  @Serializable(TotalAmountSerializer::class)
  public data object TotalAmount : TaxInvoicesSheetField {
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
  public data object TotalSupplyAmount : TaxInvoicesSheetField {
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
  public data object TotalTaxAmount : TaxInvoicesSheetField {
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
  /** 관리용 메모 */
  @Serializable(MemoSerializer::class)
  public data object Memo : TaxInvoicesSheetField {
    override val value: String = "MEMO"
  }
  public object MemoSerializer : KSerializer<Memo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Memo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Memo = decoder.decodeString().let {
      if (it != "MEMO") {
        throw SerializationException(it)
      } else {
        return Memo
      }
    }
    override fun serialize(encoder: Encoder, value: Memo): Unit = encoder.encodeString(value.value)
  }
  /** 발행요청일시 */
  @Serializable(RequestedAtSerializer::class)
  public data object RequestedAt : TaxInvoicesSheetField {
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
  public data object IssuedAt : TaxInvoicesSheetField {
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
  /** 국세청 전송일시 */
  @Serializable(NtsSentAtSerializer::class)
  public data object NtsSentAt : TaxInvoicesSheetField {
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
  public data object StatusUpdatedAt : TaxInvoicesSheetField {
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
  /** 일괄 세금계산서 아이디 */
  @Serializable(BulkTaxInvoiceIdSerializer::class)
  public data object BulkTaxInvoiceId : TaxInvoicesSheetField {
    override val value: String = "BULK_TAX_INVOICE_ID"
  }
  public object BulkTaxInvoiceIdSerializer : KSerializer<BulkTaxInvoiceId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BulkTaxInvoiceId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BulkTaxInvoiceId = decoder.decodeString().let {
      if (it != "BULK_TAX_INVOICE_ID") {
        throw SerializationException(it)
      } else {
        return BulkTaxInvoiceId
      }
    }
    override fun serialize(encoder: Encoder, value: BulkTaxInvoiceId): Unit = encoder.encodeString(value.value)
  }
  /** 세금계산서 아이디 */
  @Serializable(PlainIdSerializer::class)
  public data object PlainId : TaxInvoicesSheetField {
    override val value: String = "PLAIN_ID"
  }
  public object PlainIdSerializer : KSerializer<PlainId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlainId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PlainId = decoder.decodeString().let {
      if (it != "PLAIN_ID") {
        throw SerializationException(it)
      } else {
        return PlainId
      }
    }
    override fun serialize(encoder: Encoder, value: PlainId): Unit = encoder.encodeString(value.value)
  }
  /** 공급자 문서번호 */
  @Serializable(SupplierDocumentKeySerializer::class)
  public data object SupplierDocumentKey : TaxInvoicesSheetField {
    override val value: String = "SUPPLIER_DOCUMENT_KEY"
  }
  public object SupplierDocumentKeySerializer : KSerializer<SupplierDocumentKey> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SupplierDocumentKey::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SupplierDocumentKey = decoder.decodeString().let {
      if (it != "SUPPLIER_DOCUMENT_KEY") {
        throw SerializationException(it)
      } else {
        return SupplierDocumentKey
      }
    }
    override fun serialize(encoder: Encoder, value: SupplierDocumentKey): Unit = encoder.encodeString(value.value)
  }
  /** 공급받는자 문서번호 */
  @Serializable(RecipientDocumentKeySerializer::class)
  public data object RecipientDocumentKey : TaxInvoicesSheetField {
    override val value: String = "RECIPIENT_DOCUMENT_KEY"
  }
  public object RecipientDocumentKeySerializer : KSerializer<RecipientDocumentKey> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RecipientDocumentKey::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RecipientDocumentKey = decoder.decodeString().let {
      if (it != "RECIPIENT_DOCUMENT_KEY") {
        throw SerializationException(it)
      } else {
        return RecipientDocumentKey
      }
    }
    override fun serialize(encoder: Encoder, value: RecipientDocumentKey): Unit = encoder.encodeString(value.value)
  }
  /** 지급 아이디 */
  @Serializable(PayoutIdSerializer::class)
  public data object PayoutId : TaxInvoicesSheetField {
    override val value: String = "PAYOUT_ID"
  }
  public object PayoutIdSerializer : KSerializer<PayoutId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayoutId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayoutId = decoder.decodeString().let {
      if (it != "PAYOUT_ID") {
        throw SerializationException(it)
      } else {
        return PayoutId
      }
    }
    override fun serialize(encoder: Encoder, value: PayoutId): Unit = encoder.encodeString(value.value)
  }
  /** 품목 */
  @Serializable(ItemsSerializer::class)
  public data object Items : TaxInvoicesSheetField {
    override val value: String = "ITEMS"
  }
  public object ItemsSerializer : KSerializer<Items> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Items::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Items = decoder.decodeString().let {
      if (it != "ITEMS") {
        throw SerializationException(it)
      } else {
        return Items
      }
    }
    override fun serialize(encoder: Encoder, value: Items): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : TaxInvoicesSheetField
}


public object TaxInvoicesSheetFieldSerializer : KSerializer<TaxInvoicesSheetField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TaxInvoicesSheetField::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): TaxInvoicesSheetField {
    val value = decoder.decodeString()
    return when (value) {
      "STATUS" -> TaxInvoicesSheetField.Status
      "CANCEL_REASON" -> TaxInvoicesSheetField.CancelReason
      "ISSUANCE_TYPE" -> TaxInvoicesSheetField.IssuanceType
      "DOCUMENT_MODIFICATION_TYPE" -> TaxInvoicesSheetField.DocumentModificationType
      "IS_DELAYED" -> TaxInvoicesSheetField.IsDelayed
      "WRITE_DATE" -> TaxInvoicesSheetField.WriteDate
      "ISSUANCE_DUE_DATE" -> TaxInvoicesSheetField.IssuanceDueDate
      "TAXATION_TYPE" -> TaxInvoicesSheetField.TaxationType
      "PURPOSE_TYPE" -> TaxInvoicesSheetField.PurposeType
      "PARTNER_NAME" -> TaxInvoicesSheetField.PartnerName
      "PARTNER_BRN" -> TaxInvoicesSheetField.PartnerBrn
      "TOTAL_AMOUNT" -> TaxInvoicesSheetField.TotalAmount
      "TOTAL_SUPPLY_AMOUNT" -> TaxInvoicesSheetField.TotalSupplyAmount
      "TOTAL_TAX_AMOUNT" -> TaxInvoicesSheetField.TotalTaxAmount
      "MEMO" -> TaxInvoicesSheetField.Memo
      "REQUESTED_AT" -> TaxInvoicesSheetField.RequestedAt
      "ISSUED_AT" -> TaxInvoicesSheetField.IssuedAt
      "NTS_SENT_AT" -> TaxInvoicesSheetField.NtsSentAt
      "STATUS_UPDATED_AT" -> TaxInvoicesSheetField.StatusUpdatedAt
      "BULK_TAX_INVOICE_ID" -> TaxInvoicesSheetField.BulkTaxInvoiceId
      "PLAIN_ID" -> TaxInvoicesSheetField.PlainId
      "SUPPLIER_DOCUMENT_KEY" -> TaxInvoicesSheetField.SupplierDocumentKey
      "RECIPIENT_DOCUMENT_KEY" -> TaxInvoicesSheetField.RecipientDocumentKey
      "PAYOUT_ID" -> TaxInvoicesSheetField.PayoutId
      "ITEMS" -> TaxInvoicesSheetField.Items
      else -> TaxInvoicesSheetField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: TaxInvoicesSheetField): Unit = encoder.encodeString(value.value)
}
