package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통합검색 항목 */
@Serializable(PaymentTextSearchFieldSerializer::class)
public sealed interface PaymentTextSearchField {
  public val value: String
  @Serializable(AllSerializer::class)
  public data object All : PaymentTextSearchField {
    override val value: String = "ALL"
  }
  private object AllSerializer : KSerializer<All> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(All::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): All = decoder.decodeString().let {
      if (it != "ALL") {
        throw SerializationException(it)
      } else {
        return All
      }
    }
    override fun serialize(encoder: Encoder, value: All) = encoder.encodeString(value.value)
  }
  @Serializable(PaymentIdSerializer::class)
  public data object PaymentId : PaymentTextSearchField {
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
  @Serializable(TxIdSerializer::class)
  public data object TxId : PaymentTextSearchField {
    override val value: String = "TX_ID"
  }
  private object TxIdSerializer : KSerializer<TxId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TxId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TxId = decoder.decodeString().let {
      if (it != "TX_ID") {
        throw SerializationException(it)
      } else {
        return TxId
      }
    }
    override fun serialize(encoder: Encoder, value: TxId) = encoder.encodeString(value.value)
  }
  @Serializable(ScheduleIdSerializer::class)
  public data object ScheduleId : PaymentTextSearchField {
    override val value: String = "SCHEDULE_ID"
  }
  private object ScheduleIdSerializer : KSerializer<ScheduleId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ScheduleId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ScheduleId = decoder.decodeString().let {
      if (it != "SCHEDULE_ID") {
        throw SerializationException(it)
      } else {
        return ScheduleId
      }
    }
    override fun serialize(encoder: Encoder, value: ScheduleId) = encoder.encodeString(value.value)
  }
  @Serializable(FailReasonSerializer::class)
  public data object FailReason : PaymentTextSearchField {
    override val value: String = "FAIL_REASON"
  }
  private object FailReasonSerializer : KSerializer<FailReason> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(FailReason::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): FailReason = decoder.decodeString().let {
      if (it != "FAIL_REASON") {
        throw SerializationException(it)
      } else {
        return FailReason
      }
    }
    override fun serialize(encoder: Encoder, value: FailReason) = encoder.encodeString(value.value)
  }
  @Serializable(CardIssuerSerializer::class)
  public data object CardIssuer : PaymentTextSearchField {
    override val value: String = "CARD_ISSUER"
  }
  private object CardIssuerSerializer : KSerializer<CardIssuer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardIssuer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardIssuer = decoder.decodeString().let {
      if (it != "CARD_ISSUER") {
        throw SerializationException(it)
      } else {
        return CardIssuer
      }
    }
    override fun serialize(encoder: Encoder, value: CardIssuer) = encoder.encodeString(value.value)
  }
  @Serializable(CardAcquirerSerializer::class)
  public data object CardAcquirer : PaymentTextSearchField {
    override val value: String = "CARD_ACQUIRER"
  }
  private object CardAcquirerSerializer : KSerializer<CardAcquirer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardAcquirer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardAcquirer = decoder.decodeString().let {
      if (it != "CARD_ACQUIRER") {
        throw SerializationException(it)
      } else {
        return CardAcquirer
      }
    }
    override fun serialize(encoder: Encoder, value: CardAcquirer) = encoder.encodeString(value.value)
  }
  @Serializable(CardBinSerializer::class)
  public data object CardBin : PaymentTextSearchField {
    override val value: String = "CARD_BIN"
  }
  private object CardBinSerializer : KSerializer<CardBin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardBin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardBin = decoder.decodeString().let {
      if (it != "CARD_BIN") {
        throw SerializationException(it)
      } else {
        return CardBin
      }
    }
    override fun serialize(encoder: Encoder, value: CardBin) = encoder.encodeString(value.value)
  }
  @Serializable(CardNumberSerializer::class)
  public data object CardNumber : PaymentTextSearchField {
    override val value: String = "CARD_NUMBER"
  }
  private object CardNumberSerializer : KSerializer<CardNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardNumber = decoder.decodeString().let {
      if (it != "CARD_NUMBER") {
        throw SerializationException(it)
      } else {
        return CardNumber
      }
    }
    override fun serialize(encoder: Encoder, value: CardNumber) = encoder.encodeString(value.value)
  }
  @Serializable(CardApprovalNumberSerializer::class)
  public data object CardApprovalNumber : PaymentTextSearchField {
    override val value: String = "CARD_APPROVAL_NUMBER"
  }
  private object CardApprovalNumberSerializer : KSerializer<CardApprovalNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardApprovalNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardApprovalNumber = decoder.decodeString().let {
      if (it != "CARD_APPROVAL_NUMBER") {
        throw SerializationException(it)
      } else {
        return CardApprovalNumber
      }
    }
    override fun serialize(encoder: Encoder, value: CardApprovalNumber) = encoder.encodeString(value.value)
  }
  @Serializable(CardReceiptNameSerializer::class)
  public data object CardReceiptName : PaymentTextSearchField {
    override val value: String = "CARD_RECEIPT_NAME"
  }
  private object CardReceiptNameSerializer : KSerializer<CardReceiptName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardReceiptName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardReceiptName = decoder.decodeString().let {
      if (it != "CARD_RECEIPT_NAME") {
        throw SerializationException(it)
      } else {
        return CardReceiptName
      }
    }
    override fun serialize(encoder: Encoder, value: CardReceiptName) = encoder.encodeString(value.value)
  }
  @Serializable(CardInstallmentSerializer::class)
  public data object CardInstallment : PaymentTextSearchField {
    override val value: String = "CARD_INSTALLMENT"
  }
  private object CardInstallmentSerializer : KSerializer<CardInstallment> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardInstallment::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CardInstallment = decoder.decodeString().let {
      if (it != "CARD_INSTALLMENT") {
        throw SerializationException(it)
      } else {
        return CardInstallment
      }
    }
    override fun serialize(encoder: Encoder, value: CardInstallment) = encoder.encodeString(value.value)
  }
  @Serializable(TransBankSerializer::class)
  public data object TransBank : PaymentTextSearchField {
    override val value: String = "TRANS_BANK"
  }
  private object TransBankSerializer : KSerializer<TransBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TransBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TransBank = decoder.decodeString().let {
      if (it != "TRANS_BANK") {
        throw SerializationException(it)
      } else {
        return TransBank
      }
    }
    override fun serialize(encoder: Encoder, value: TransBank) = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountHolderNameSerializer::class)
  public data object VirtualAccountHolderName : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_HOLDER_NAME"
  }
  private object VirtualAccountHolderNameSerializer : KSerializer<VirtualAccountHolderName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountHolderName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountHolderName = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_HOLDER_NAME") {
        throw SerializationException(it)
      } else {
        return VirtualAccountHolderName
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountHolderName) = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountBankSerializer::class)
  public data object VirtualAccountBank : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_BANK"
  }
  private object VirtualAccountBankSerializer : KSerializer<VirtualAccountBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountBank = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_BANK") {
        throw SerializationException(it)
      } else {
        return VirtualAccountBank
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountBank) = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountNumberSerializer::class)
  public data object VirtualAccountNumber : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_NUMBER"
  }
  private object VirtualAccountNumberSerializer : KSerializer<VirtualAccountNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountNumber = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_NUMBER") {
        throw SerializationException(it)
      } else {
        return VirtualAccountNumber
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountNumber) = encoder.encodeString(value.value)
  }
  @Serializable(PgMerchantIdSerializer::class)
  public data object PgMerchantId : PaymentTextSearchField {
    override val value: String = "PG_MERCHANT_ID"
  }
  private object PgMerchantIdSerializer : KSerializer<PgMerchantId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgMerchantId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PgMerchantId = decoder.decodeString().let {
      if (it != "PG_MERCHANT_ID") {
        throw SerializationException(it)
      } else {
        return PgMerchantId
      }
    }
    override fun serialize(encoder: Encoder, value: PgMerchantId) = encoder.encodeString(value.value)
  }
  @Serializable(PgTxIdSerializer::class)
  public data object PgTxId : PaymentTextSearchField {
    override val value: String = "PG_TX_ID"
  }
  private object PgTxIdSerializer : KSerializer<PgTxId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgTxId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PgTxId = decoder.decodeString().let {
      if (it != "PG_TX_ID") {
        throw SerializationException(it)
      } else {
        return PgTxId
      }
    }
    override fun serialize(encoder: Encoder, value: PgTxId) = encoder.encodeString(value.value)
  }
  @Serializable(PgReceiptIdSerializer::class)
  public data object PgReceiptId : PaymentTextSearchField {
    override val value: String = "PG_RECEIPT_ID"
  }
  private object PgReceiptIdSerializer : KSerializer<PgReceiptId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgReceiptId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PgReceiptId = decoder.decodeString().let {
      if (it != "PG_RECEIPT_ID") {
        throw SerializationException(it)
      } else {
        return PgReceiptId
      }
    }
    override fun serialize(encoder: Encoder, value: PgReceiptId) = encoder.encodeString(value.value)
  }
  @Serializable(ReceiptApprovalNumberSerializer::class)
  public data object ReceiptApprovalNumber : PaymentTextSearchField {
    override val value: String = "RECEIPT_APPROVAL_NUMBER"
  }
  private object ReceiptApprovalNumberSerializer : KSerializer<ReceiptApprovalNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ReceiptApprovalNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ReceiptApprovalNumber = decoder.decodeString().let {
      if (it != "RECEIPT_APPROVAL_NUMBER") {
        throw SerializationException(it)
      } else {
        return ReceiptApprovalNumber
      }
    }
    override fun serialize(encoder: Encoder, value: ReceiptApprovalNumber) = encoder.encodeString(value.value)
  }
  @Serializable(PgCancellationIdSerializer::class)
  public data object PgCancellationId : PaymentTextSearchField {
    override val value: String = "PG_CANCELLATION_ID"
  }
  private object PgCancellationIdSerializer : KSerializer<PgCancellationId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgCancellationId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PgCancellationId = decoder.decodeString().let {
      if (it != "PG_CANCELLATION_ID") {
        throw SerializationException(it)
      } else {
        return PgCancellationId
      }
    }
    override fun serialize(encoder: Encoder, value: PgCancellationId) = encoder.encodeString(value.value)
  }
  @Serializable(CancelReasonSerializer::class)
  public data object CancelReason : PaymentTextSearchField {
    override val value: String = "CANCEL_REASON"
  }
  private object CancelReasonSerializer : KSerializer<CancelReason> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelReason::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CancelReason = decoder.decodeString().let {
      if (it != "CANCEL_REASON") {
        throw SerializationException(it)
      } else {
        return CancelReason
      }
    }
    override fun serialize(encoder: Encoder, value: CancelReason) = encoder.encodeString(value.value)
  }
  @Serializable(OrderNameSerializer::class)
  public data object OrderName : PaymentTextSearchField {
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
  @Serializable(CustomerNameSerializer::class)
  public data object CustomerName : PaymentTextSearchField {
    override val value: String = "CUSTOMER_NAME"
  }
  private object CustomerNameSerializer : KSerializer<CustomerName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CustomerName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CustomerName = decoder.decodeString().let {
      if (it != "CUSTOMER_NAME") {
        throw SerializationException(it)
      } else {
        return CustomerName
      }
    }
    override fun serialize(encoder: Encoder, value: CustomerName) = encoder.encodeString(value.value)
  }
  @Serializable(CustomerEmailSerializer::class)
  public data object CustomerEmail : PaymentTextSearchField {
    override val value: String = "CUSTOMER_EMAIL"
  }
  private object CustomerEmailSerializer : KSerializer<CustomerEmail> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CustomerEmail::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CustomerEmail = decoder.decodeString().let {
      if (it != "CUSTOMER_EMAIL") {
        throw SerializationException(it)
      } else {
        return CustomerEmail
      }
    }
    override fun serialize(encoder: Encoder, value: CustomerEmail) = encoder.encodeString(value.value)
  }
  @Serializable(CustomerPhoneNumberSerializer::class)
  public data object CustomerPhoneNumber : PaymentTextSearchField {
    override val value: String = "CUSTOMER_PHONE_NUMBER"
  }
  private object CustomerPhoneNumberSerializer : KSerializer<CustomerPhoneNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CustomerPhoneNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CustomerPhoneNumber = decoder.decodeString().let {
      if (it != "CUSTOMER_PHONE_NUMBER") {
        throw SerializationException(it)
      } else {
        return CustomerPhoneNumber
      }
    }
    override fun serialize(encoder: Encoder, value: CustomerPhoneNumber) = encoder.encodeString(value.value)
  }
  @Serializable(CustomerAddressSerializer::class)
  public data object CustomerAddress : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ADDRESS"
  }
  private object CustomerAddressSerializer : KSerializer<CustomerAddress> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CustomerAddress::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CustomerAddress = decoder.decodeString().let {
      if (it != "CUSTOMER_ADDRESS") {
        throw SerializationException(it)
      } else {
        return CustomerAddress
      }
    }
    override fun serialize(encoder: Encoder, value: CustomerAddress) = encoder.encodeString(value.value)
  }
  @Serializable(CustomerZipcodeSerializer::class)
  public data object CustomerZipcode : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ZIPCODE"
  }
  private object CustomerZipcodeSerializer : KSerializer<CustomerZipcode> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CustomerZipcode::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CustomerZipcode = decoder.decodeString().let {
      if (it != "CUSTOMER_ZIPCODE") {
        throw SerializationException(it)
      } else {
        return CustomerZipcode
      }
    }
    override fun serialize(encoder: Encoder, value: CustomerZipcode) = encoder.encodeString(value.value)
  }
  @Serializable(UserAgentSerializer::class)
  public data object UserAgent : PaymentTextSearchField {
    override val value: String = "USER_AGENT"
  }
  private object UserAgentSerializer : KSerializer<UserAgent> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(UserAgent::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): UserAgent = decoder.decodeString().let {
      if (it != "USER_AGENT") {
        throw SerializationException(it)
      } else {
        return UserAgent
      }
    }
    override fun serialize(encoder: Encoder, value: UserAgent) = encoder.encodeString(value.value)
  }
  @Serializable(BillingKeySerializer::class)
  public data object BillingKey : PaymentTextSearchField {
    override val value: String = "BILLING_KEY"
  }
  private object BillingKeySerializer : KSerializer<BillingKey> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKey::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BillingKey = decoder.decodeString().let {
      if (it != "BILLING_KEY") {
        throw SerializationException(it)
      } else {
        return BillingKey
      }
    }
    override fun serialize(encoder: Encoder, value: BillingKey) = encoder.encodeString(value.value)
  }
  @Serializable(PromotionIdSerializer::class)
  public data object PromotionId : PaymentTextSearchField {
    override val value: String = "PROMOTION_ID"
  }
  private object PromotionIdSerializer : KSerializer<PromotionId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PromotionId = decoder.decodeString().let {
      if (it != "PROMOTION_ID") {
        throw SerializationException(it)
      } else {
        return PromotionId
      }
    }
    override fun serialize(encoder: Encoder, value: PromotionId) = encoder.encodeString(value.value)
  }
  @Serializable(GiftCertificationApprovalNumberSerializer::class)
  public data object GiftCertificationApprovalNumber : PaymentTextSearchField {
    override val value: String = "GIFT_CERTIFICATION_APPROVAL_NUMBER"
  }
  private object GiftCertificationApprovalNumberSerializer : KSerializer<GiftCertificationApprovalNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GiftCertificationApprovalNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GiftCertificationApprovalNumber = decoder.decodeString().let {
      if (it != "GIFT_CERTIFICATION_APPROVAL_NUMBER") {
        throw SerializationException(it)
      } else {
        return GiftCertificationApprovalNumber
      }
    }
    override fun serialize(encoder: Encoder, value: GiftCertificationApprovalNumber) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentTextSearchField
}


private object PaymentTextSearchFieldSerializer : KSerializer<PaymentTextSearchField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentTextSearchField::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentTextSearchField {
    val value = decoder.decodeString()
    return when (value) {
      "ALL" -> PaymentTextSearchField.All
      "PAYMENT_ID" -> PaymentTextSearchField.PaymentId
      "TX_ID" -> PaymentTextSearchField.TxId
      "SCHEDULE_ID" -> PaymentTextSearchField.ScheduleId
      "FAIL_REASON" -> PaymentTextSearchField.FailReason
      "CARD_ISSUER" -> PaymentTextSearchField.CardIssuer
      "CARD_ACQUIRER" -> PaymentTextSearchField.CardAcquirer
      "CARD_BIN" -> PaymentTextSearchField.CardBin
      "CARD_NUMBER" -> PaymentTextSearchField.CardNumber
      "CARD_APPROVAL_NUMBER" -> PaymentTextSearchField.CardApprovalNumber
      "CARD_RECEIPT_NAME" -> PaymentTextSearchField.CardReceiptName
      "CARD_INSTALLMENT" -> PaymentTextSearchField.CardInstallment
      "TRANS_BANK" -> PaymentTextSearchField.TransBank
      "VIRTUAL_ACCOUNT_HOLDER_NAME" -> PaymentTextSearchField.VirtualAccountHolderName
      "VIRTUAL_ACCOUNT_BANK" -> PaymentTextSearchField.VirtualAccountBank
      "VIRTUAL_ACCOUNT_NUMBER" -> PaymentTextSearchField.VirtualAccountNumber
      "PG_MERCHANT_ID" -> PaymentTextSearchField.PgMerchantId
      "PG_TX_ID" -> PaymentTextSearchField.PgTxId
      "PG_RECEIPT_ID" -> PaymentTextSearchField.PgReceiptId
      "RECEIPT_APPROVAL_NUMBER" -> PaymentTextSearchField.ReceiptApprovalNumber
      "PG_CANCELLATION_ID" -> PaymentTextSearchField.PgCancellationId
      "CANCEL_REASON" -> PaymentTextSearchField.CancelReason
      "ORDER_NAME" -> PaymentTextSearchField.OrderName
      "CUSTOMER_NAME" -> PaymentTextSearchField.CustomerName
      "CUSTOMER_EMAIL" -> PaymentTextSearchField.CustomerEmail
      "CUSTOMER_PHONE_NUMBER" -> PaymentTextSearchField.CustomerPhoneNumber
      "CUSTOMER_ADDRESS" -> PaymentTextSearchField.CustomerAddress
      "CUSTOMER_ZIPCODE" -> PaymentTextSearchField.CustomerZipcode
      "USER_AGENT" -> PaymentTextSearchField.UserAgent
      "BILLING_KEY" -> PaymentTextSearchField.BillingKey
      "PROMOTION_ID" -> PaymentTextSearchField.PromotionId
      "GIFT_CERTIFICATION_APPROVAL_NUMBER" -> PaymentTextSearchField.GiftCertificationApprovalNumber
      else -> PaymentTextSearchField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentTextSearchField) = encoder.encodeString(value.value)
}
