package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 수정 사유 */
@Serializable(B2bTaxInvoiceModificationTypeSerializer::class)
public sealed interface B2bTaxInvoiceModificationType {
  public val value: String
  /** 기재사항 착오 정정 */
  @Serializable(CorrectionOfEntryErrorsSerializer::class)
  public data object CorrectionOfEntryErrors : B2bTaxInvoiceModificationType {
    override val value: String = "CORRECTION_OF_ENTRY_ERRORS"
  }
  private object CorrectionOfEntryErrorsSerializer : KSerializer<CorrectionOfEntryErrors> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CorrectionOfEntryErrors::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CorrectionOfEntryErrors = decoder.decodeString().let {
      if (it != "CORRECTION_OF_ENTRY_ERRORS") {
        throw SerializationException(it)
      } else {
        return CorrectionOfEntryErrors
      }
    }
    override fun serialize(encoder: Encoder, value: CorrectionOfEntryErrors) = encoder.encodeString(value.value)
  }
  /** 공금가액 변동 */
  @Serializable(ChangeInSupplyCostSerializer::class)
  public data object ChangeInSupplyCost : B2bTaxInvoiceModificationType {
    override val value: String = "CHANGE_IN_SUPPLY_COST"
  }
  private object ChangeInSupplyCostSerializer : KSerializer<ChangeInSupplyCost> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ChangeInSupplyCost::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ChangeInSupplyCost = decoder.decodeString().let {
      if (it != "CHANGE_IN_SUPPLY_COST") {
        throw SerializationException(it)
      } else {
        return ChangeInSupplyCost
      }
    }
    override fun serialize(encoder: Encoder, value: ChangeInSupplyCost) = encoder.encodeString(value.value)
  }
  /** 환입 */
  @Serializable(ReturnSerializer::class)
  public data object Return : B2bTaxInvoiceModificationType {
    override val value: String = "RETURN"
  }
  private object ReturnSerializer : KSerializer<Return> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Return::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Return = decoder.decodeString().let {
      if (it != "RETURN") {
        throw SerializationException(it)
      } else {
        return Return
      }
    }
    override fun serialize(encoder: Encoder, value: Return) = encoder.encodeString(value.value)
  }
  /** 계약 해제 */
  @Serializable(CancellationOfContractSerializer::class)
  public data object CancellationOfContract : B2bTaxInvoiceModificationType {
    override val value: String = "CANCELLATION_OF_CONTRACT"
  }
  private object CancellationOfContractSerializer : KSerializer<CancellationOfContract> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancellationOfContract::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CancellationOfContract = decoder.decodeString().let {
      if (it != "CANCELLATION_OF_CONTRACT") {
        throw SerializationException(it)
      } else {
        return CancellationOfContract
      }
    }
    override fun serialize(encoder: Encoder, value: CancellationOfContract) = encoder.encodeString(value.value)
  }
  /** 착오에 의한 이중 발급 */
  @Serializable(DuplicateIssuanceDueToErrorSerializer::class)
  public data object DuplicateIssuanceDueToError : B2bTaxInvoiceModificationType {
    override val value: String = "DUPLICATE_ISSUANCE_DUE_TO_ERROR"
  }
  private object DuplicateIssuanceDueToErrorSerializer : KSerializer<DuplicateIssuanceDueToError> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DuplicateIssuanceDueToError::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DuplicateIssuanceDueToError = decoder.decodeString().let {
      if (it != "DUPLICATE_ISSUANCE_DUE_TO_ERROR") {
        throw SerializationException(it)
      } else {
        return DuplicateIssuanceDueToError
      }
    }
    override fun serialize(encoder: Encoder, value: DuplicateIssuanceDueToError) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceModificationType
}


private object B2bTaxInvoiceModificationTypeSerializer : KSerializer<B2bTaxInvoiceModificationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceModificationType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceModificationType {
    val value = decoder.decodeString()
    return when (value) {
      "CORRECTION_OF_ENTRY_ERRORS" -> B2bTaxInvoiceModificationType.CorrectionOfEntryErrors
      "CHANGE_IN_SUPPLY_COST" -> B2bTaxInvoiceModificationType.ChangeInSupplyCost
      "RETURN" -> B2bTaxInvoiceModificationType.Return
      "CANCELLATION_OF_CONTRACT" -> B2bTaxInvoiceModificationType.CancellationOfContract
      "DUPLICATE_ISSUANCE_DUE_TO_ERROR" -> B2bTaxInvoiceModificationType.DuplicateIssuanceDueToError
      else -> B2bTaxInvoiceModificationType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceModificationType) = encoder.encodeString(value.value)
}
