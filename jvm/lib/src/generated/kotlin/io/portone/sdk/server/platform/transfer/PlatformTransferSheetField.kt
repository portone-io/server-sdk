package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 다운로드 할 시트 컬럼 */
@Serializable(PlatformTransferSheetFieldSerializer::class)
public sealed interface PlatformTransferSheetField {
  public val value: String
  /** 정산 건 상태 */
  @Serializable(StatusSerializer::class)
  public data object Status : PlatformTransferSheetField {
    override val value: String = "STATUS"
  }
  private object StatusSerializer : KSerializer<Status> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Status::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Status = decoder.decodeString().let {
      if (it != "STATUS") {
        throw SerializationException(it)
      } else {
        return Status
      }
    }
    override fun serialize(encoder: Encoder, value: Status) = encoder.encodeString(value.value)
  }
  /** 정산 건 아이디 */
  @Serializable(TransferIdSerializer::class)
  public data object TransferId : PlatformTransferSheetField {
    override val value: String = "TRANSFER_ID"
  }
  private object TransferIdSerializer : KSerializer<TransferId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TransferId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TransferId = decoder.decodeString().let {
      if (it != "TRANSFER_ID") {
        throw SerializationException(it)
      } else {
        return TransferId
      }
    }
    override fun serialize(encoder: Encoder, value: TransferId) = encoder.encodeString(value.value)
  }
  /** 파트너 이름 */
  @Serializable(PartnerNameSerializer::class)
  public data object PartnerName : PlatformTransferSheetField {
    override val value: String = "PARTNER_NAME"
  }
  private object PartnerNameSerializer : KSerializer<PartnerName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerName = decoder.decodeString().let {
      if (it != "PARTNER_NAME") {
        throw SerializationException(it)
      } else {
        return PartnerName
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerName) = encoder.encodeString(value.value)
  }
  /** 정산 일 */
  @Serializable(SettlementDateSerializer::class)
  public data object SettlementDate : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DATE"
  }
  private object SettlementDateSerializer : KSerializer<SettlementDate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementDate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementDate = decoder.decodeString().let {
      if (it != "SETTLEMENT_DATE") {
        throw SerializationException(it)
      } else {
        return SettlementDate
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementDate) = encoder.encodeString(value.value)
  }
  /** 정산 시작 일 */
  @Serializable(SettlementStartDateSerializer::class)
  public data object SettlementStartDate : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_START_DATE"
  }
  private object SettlementStartDateSerializer : KSerializer<SettlementStartDate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementStartDate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementStartDate = decoder.decodeString().let {
      if (it != "SETTLEMENT_START_DATE") {
        throw SerializationException(it)
      } else {
        return SettlementStartDate
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementStartDate) = encoder.encodeString(value.value)
  }
  /** 정산 구분 */
  @Serializable(TypeSerializer::class)
  public data object Type : PlatformTransferSheetField {
    override val value: String = "TYPE"
  }
  private object TypeSerializer : KSerializer<Type> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Type::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Type = decoder.decodeString().let {
      if (it != "TYPE") {
        throw SerializationException(it)
      } else {
        return Type
      }
    }
    override fun serialize(encoder: Encoder, value: Type) = encoder.encodeString(value.value)
  }
  /** 결제 내역 아이디 */
  @Serializable(PaymentIdSerializer::class)
  public data object PaymentId : PlatformTransferSheetField {
    override val value: String = "PAYMENT_ID"
  }
  private object PaymentIdSerializer : KSerializer<PaymentId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PaymentId = decoder.decodeString().let {
      if (it != "PAYMENT_ID") {
        throw SerializationException(it)
      } else {
        return PaymentId
      }
    }
    override fun serialize(encoder: Encoder, value: PaymentId) = encoder.encodeString(value.value)
  }
  /** 주문 명 */
  @Serializable(OrderNameSerializer::class)
  public data object OrderName : PlatformTransferSheetField {
    override val value: String = "ORDER_NAME"
  }
  private object OrderNameSerializer : KSerializer<OrderName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(OrderName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): OrderName = decoder.decodeString().let {
      if (it != "ORDER_NAME") {
        throw SerializationException(it)
      } else {
        return OrderName
      }
    }
    override fun serialize(encoder: Encoder, value: OrderName) = encoder.encodeString(value.value)
  }
  /** 결제 수단 */
  @Serializable(PaymentMethodSerializer::class)
  public data object PaymentMethod : PlatformTransferSheetField {
    override val value: String = "PAYMENT_METHOD"
  }
  private object PaymentMethodSerializer : KSerializer<PaymentMethod> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethod::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PaymentMethod = decoder.decodeString().let {
      if (it != "PAYMENT_METHOD") {
        throw SerializationException(it)
      } else {
        return PaymentMethod
      }
    }
    override fun serialize(encoder: Encoder, value: PaymentMethod) = encoder.encodeString(value.value)
  }
  /** 정산 금액 */
  @Serializable(SettlementAmountSerializer::class)
  public data object SettlementAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_AMOUNT"
  }
  private object SettlementAmountSerializer : KSerializer<SettlementAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementAmount) = encoder.encodeString(value.value)
  }
  /** 주문 금액 */
  @Serializable(SettlementOrderAmountSerializer::class)
  public data object SettlementOrderAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ORDER_AMOUNT"
  }
  private object SettlementOrderAmountSerializer : KSerializer<SettlementOrderAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementOrderAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementOrderAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_ORDER_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementOrderAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementOrderAmount) = encoder.encodeString(value.value)
  }
  /** 면세 주문 금액 */
  @Serializable(SettlementOrderTaxFreeAmountSerializer::class)
  public data object SettlementOrderTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ORDER_TAX_FREE_AMOUNT"
  }
  private object SettlementOrderTaxFreeAmountSerializer : KSerializer<SettlementOrderTaxFreeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementOrderTaxFreeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementOrderTaxFreeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_ORDER_TAX_FREE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementOrderTaxFreeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementOrderTaxFreeAmount) = encoder.encodeString(value.value)
  }
  /** 결제 금액 */
  @Serializable(SettlementPaymentAmountSerializer::class)
  public data object SettlementPaymentAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_AMOUNT"
  }
  private object SettlementPaymentAmountSerializer : KSerializer<SettlementPaymentAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPaymentAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPaymentAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PAYMENT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPaymentAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPaymentAmount) = encoder.encodeString(value.value)
  }
  /** 결제 금액 부가세 */
  @Serializable(SettlementPaymentVatAmountSerializer::class)
  public data object SettlementPaymentVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_VAT_AMOUNT"
  }
  private object SettlementPaymentVatAmountSerializer : KSerializer<SettlementPaymentVatAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPaymentVatAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPaymentVatAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PAYMENT_VAT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPaymentVatAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPaymentVatAmount) = encoder.encodeString(value.value)
  }
  /** 결제 금액 부가세 부담금 */
  @Serializable(SettlementPaymentVatBurdenAmountSerializer::class)
  public data object SettlementPaymentVatBurdenAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT"
  }
  private object SettlementPaymentVatBurdenAmountSerializer : KSerializer<SettlementPaymentVatBurdenAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPaymentVatBurdenAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPaymentVatBurdenAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPaymentVatBurdenAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPaymentVatBurdenAmount) = encoder.encodeString(value.value)
  }
  /** 결제 공급가액 */
  @Serializable(SettlementPaymentSupplyAmountSerializer::class)
  public data object SettlementPaymentSupplyAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT"
  }
  private object SettlementPaymentSupplyAmountSerializer : KSerializer<SettlementPaymentSupplyAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPaymentSupplyAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPaymentSupplyAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPaymentSupplyAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPaymentSupplyAmount) = encoder.encodeString(value.value)
  }
  /** 결제 면세액 */
  @Serializable(SettlementPaymentTaxFreeAmountSerializer::class)
  public data object SettlementPaymentTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT"
  }
  private object SettlementPaymentTaxFreeAmountSerializer : KSerializer<SettlementPaymentTaxFreeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPaymentTaxFreeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPaymentTaxFreeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPaymentTaxFreeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPaymentTaxFreeAmount) = encoder.encodeString(value.value)
  }
  /** 중개 수수료 */
  @Serializable(SettlementPlatformFeeAmountSerializer::class)
  public data object SettlementPlatformFeeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PLATFORM_FEE_AMOUNT"
  }
  private object SettlementPlatformFeeAmountSerializer : KSerializer<SettlementPlatformFeeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPlatformFeeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPlatformFeeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PLATFORM_FEE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPlatformFeeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPlatformFeeAmount) = encoder.encodeString(value.value)
  }
  /** 중개 수수료 부가세 */
  @Serializable(SettlementPlatformFeeVatAmountSerializer::class)
  public data object SettlementPlatformFeeVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT"
  }
  private object SettlementPlatformFeeVatAmountSerializer : KSerializer<SettlementPlatformFeeVatAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementPlatformFeeVatAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementPlatformFeeVatAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementPlatformFeeVatAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementPlatformFeeVatAmount) = encoder.encodeString(value.value)
  }
  /** 할인 금액 */
  @Serializable(SettlementDiscountAmountSerializer::class)
  public data object SettlementDiscountAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_AMOUNT"
  }
  private object SettlementDiscountAmountSerializer : KSerializer<SettlementDiscountAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementDiscountAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementDiscountAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_DISCOUNT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementDiscountAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementDiscountAmount) = encoder.encodeString(value.value)
  }
  /** 면세 할인 금액 */
  @Serializable(SettlementDiscountTaxFreeAmountSerializer::class)
  public data object SettlementDiscountTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT"
  }
  private object SettlementDiscountTaxFreeAmountSerializer : KSerializer<SettlementDiscountTaxFreeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementDiscountTaxFreeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementDiscountTaxFreeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementDiscountTaxFreeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementDiscountTaxFreeAmount) = encoder.encodeString(value.value)
  }
  /** 할인 분담금 */
  @Serializable(SettlementDiscountShareAmountSerializer::class)
  public data object SettlementDiscountShareAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_SHARE_AMOUNT"
  }
  private object SettlementDiscountShareAmountSerializer : KSerializer<SettlementDiscountShareAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementDiscountShareAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementDiscountShareAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_DISCOUNT_SHARE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementDiscountShareAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementDiscountShareAmount) = encoder.encodeString(value.value)
  }
  /** 면세 할인 분담금 */
  @Serializable(SettlementDiscountShareTaxFreeAmountSerializer::class)
  public data object SettlementDiscountShareTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT"
  }
  private object SettlementDiscountShareTaxFreeAmountSerializer : KSerializer<SettlementDiscountShareTaxFreeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementDiscountShareTaxFreeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementDiscountShareTaxFreeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementDiscountShareTaxFreeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementDiscountShareTaxFreeAmount) = encoder.encodeString(value.value)
  }
  /** 추가 수수료 */
  @Serializable(SettlementAdditionalFeeAmountSerializer::class)
  public data object SettlementAdditionalFeeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ADDITIONAL_FEE_AMOUNT"
  }
  private object SettlementAdditionalFeeAmountSerializer : KSerializer<SettlementAdditionalFeeAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementAdditionalFeeAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementAdditionalFeeAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_ADDITIONAL_FEE_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementAdditionalFeeAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementAdditionalFeeAmount) = encoder.encodeString(value.value)
  }
  /** 추가 수수료 부가세 */
  @Serializable(SettlementAdditionalFeeVatAmountSerializer::class)
  public data object SettlementAdditionalFeeVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT"
  }
  private object SettlementAdditionalFeeVatAmountSerializer : KSerializer<SettlementAdditionalFeeVatAmount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementAdditionalFeeVatAmount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementAdditionalFeeVatAmount = decoder.decodeString().let {
      if (it != "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT") {
        throw SerializationException(it)
      } else {
        return SettlementAdditionalFeeVatAmount
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementAdditionalFeeVatAmount) = encoder.encodeString(value.value)
  }
  /** 정산 통화 */
  @Serializable(SettlementCurrencySerializer::class)
  public data object SettlementCurrency : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_CURRENCY"
  }
  private object SettlementCurrencySerializer : KSerializer<SettlementCurrency> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementCurrency::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SettlementCurrency = decoder.decodeString().let {
      if (it != "SETTLEMENT_CURRENCY") {
        throw SerializationException(it)
      } else {
        return SettlementCurrency
      }
    }
    override fun serialize(encoder: Encoder, value: SettlementCurrency) = encoder.encodeString(value.value)
  }
  /** 파트너 유형 */
  @Serializable(PartnerTypeSerializer::class)
  public data object PartnerType : PlatformTransferSheetField {
    override val value: String = "PARTNER_TYPE"
  }
  private object PartnerTypeSerializer : KSerializer<PartnerType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerType = decoder.decodeString().let {
      if (it != "PARTNER_TYPE") {
        throw SerializationException(it)
      } else {
        return PartnerType
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerType) = encoder.encodeString(value.value)
  }
  /** 파트너 과세 유형 */
  @Serializable(PartnerTaxationTypeSerializer::class)
  public data object PartnerTaxationType : PlatformTransferSheetField {
    override val value: String = "PARTNER_TAXATION_TYPE"
  }
  private object PartnerTaxationTypeSerializer : KSerializer<PartnerTaxationType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerTaxationType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerTaxationType = decoder.decodeString().let {
      if (it != "PARTNER_TAXATION_TYPE") {
        throw SerializationException(it)
      } else {
        return PartnerTaxationType
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerTaxationType) = encoder.encodeString(value.value)
  }
  /** 파트너 소득 유형 */
  @Serializable(PartnerIncomeTypeSerializer::class)
  public data object PartnerIncomeType : PlatformTransferSheetField {
    override val value: String = "PARTNER_INCOME_TYPE"
  }
  private object PartnerIncomeTypeSerializer : KSerializer<PartnerIncomeType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerIncomeType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerIncomeType = decoder.decodeString().let {
      if (it != "PARTNER_INCOME_TYPE") {
        throw SerializationException(it)
      } else {
        return PartnerIncomeType
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerIncomeType) = encoder.encodeString(value.value)
  }
  /**
   * 파트너 과세 유형 또는 소득 유형
   *
   * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
   */
  @Serializable(PartnerTaxationTypeOrIncomeTypeSerializer::class)
  public data object PartnerTaxationTypeOrIncomeType : PlatformTransferSheetField {
    override val value: String = "PARTNER_TAXATION_TYPE_OR_INCOME_TYPE"
  }
  private object PartnerTaxationTypeOrIncomeTypeSerializer : KSerializer<PartnerTaxationTypeOrIncomeType> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerTaxationTypeOrIncomeType::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerTaxationTypeOrIncomeType = decoder.decodeString().let {
      if (it != "PARTNER_TAXATION_TYPE_OR_INCOME_TYPE") {
        throw SerializationException(it)
      } else {
        return PartnerTaxationTypeOrIncomeType
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerTaxationTypeOrIncomeType) = encoder.encodeString(value.value)
  }
  /** 파트너 아이디 */
  @Serializable(PartnerIdSerializer::class)
  public data object PartnerId : PlatformTransferSheetField {
    override val value: String = "PARTNER_ID"
  }
  private object PartnerIdSerializer : KSerializer<PartnerId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerId = decoder.decodeString().let {
      if (it != "PARTNER_ID") {
        throw SerializationException(it)
      } else {
        return PartnerId
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerId) = encoder.encodeString(value.value)
  }
  /** 메모 */
  @Serializable(MemoSerializer::class)
  public data object Memo : PlatformTransferSheetField {
    override val value: String = "MEMO"
  }
  private object MemoSerializer : KSerializer<Memo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Memo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Memo = decoder.decodeString().let {
      if (it != "MEMO") {
        throw SerializationException(it)
      } else {
        return Memo
      }
    }
    override fun serialize(encoder: Encoder, value: Memo) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferSheetField
}


private object PlatformTransferSheetFieldSerializer : KSerializer<PlatformTransferSheetField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferSheetField::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferSheetField {
    val value = decoder.decodeString()
    return when (value) {
      "STATUS" -> PlatformTransferSheetField.Status
      "TRANSFER_ID" -> PlatformTransferSheetField.TransferId
      "PARTNER_NAME" -> PlatformTransferSheetField.PartnerName
      "SETTLEMENT_DATE" -> PlatformTransferSheetField.SettlementDate
      "SETTLEMENT_START_DATE" -> PlatformTransferSheetField.SettlementStartDate
      "TYPE" -> PlatformTransferSheetField.Type
      "PAYMENT_ID" -> PlatformTransferSheetField.PaymentId
      "ORDER_NAME" -> PlatformTransferSheetField.OrderName
      "PAYMENT_METHOD" -> PlatformTransferSheetField.PaymentMethod
      "SETTLEMENT_AMOUNT" -> PlatformTransferSheetField.SettlementAmount
      "SETTLEMENT_ORDER_AMOUNT" -> PlatformTransferSheetField.SettlementOrderAmount
      "SETTLEMENT_ORDER_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementOrderTaxFreeAmount
      "SETTLEMENT_PAYMENT_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentAmount
      "SETTLEMENT_PAYMENT_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentVatAmount
      "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentVatBurdenAmount
      "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentSupplyAmount
      "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentTaxFreeAmount
      "SETTLEMENT_PLATFORM_FEE_AMOUNT" -> PlatformTransferSheetField.SettlementPlatformFeeAmount
      "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementPlatformFeeVatAmount
      "SETTLEMENT_DISCOUNT_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountAmount
      "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountTaxFreeAmount
      "SETTLEMENT_DISCOUNT_SHARE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountShareAmount
      "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountShareTaxFreeAmount
      "SETTLEMENT_ADDITIONAL_FEE_AMOUNT" -> PlatformTransferSheetField.SettlementAdditionalFeeAmount
      "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementAdditionalFeeVatAmount
      "SETTLEMENT_CURRENCY" -> PlatformTransferSheetField.SettlementCurrency
      "PARTNER_TYPE" -> PlatformTransferSheetField.PartnerType
      "PARTNER_TAXATION_TYPE" -> PlatformTransferSheetField.PartnerTaxationType
      "PARTNER_INCOME_TYPE" -> PlatformTransferSheetField.PartnerIncomeType
      "PARTNER_TAXATION_TYPE_OR_INCOME_TYPE" -> PlatformTransferSheetField.PartnerTaxationTypeOrIncomeType
      "PARTNER_ID" -> PlatformTransferSheetField.PartnerId
      "MEMO" -> PlatformTransferSheetField.Memo
      else -> PlatformTransferSheetField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferSheetField) = encoder.encodeString(value.value)
}
