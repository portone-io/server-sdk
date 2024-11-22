package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통합검색 항목 */
@Serializable(PaymentTextSearchFieldSerializer::class)
public sealed interface PaymentTextSearchField {
  public val value: String
  public data object All : PaymentTextSearchField {
    override val value: String = "ALL"
  }
  public data object PaymentId : PaymentTextSearchField {
    override val value: String = "PAYMENT_ID"
  }
  public data object TxId : PaymentTextSearchField {
    override val value: String = "TX_ID"
  }
  public data object ScheduleId : PaymentTextSearchField {
    override val value: String = "SCHEDULE_ID"
  }
  public data object FailReason : PaymentTextSearchField {
    override val value: String = "FAIL_REASON"
  }
  public data object CardIssuer : PaymentTextSearchField {
    override val value: String = "CARD_ISSUER"
  }
  public data object CardAcquirer : PaymentTextSearchField {
    override val value: String = "CARD_ACQUIRER"
  }
  public data object CardBin : PaymentTextSearchField {
    override val value: String = "CARD_BIN"
  }
  public data object CardNumber : PaymentTextSearchField {
    override val value: String = "CARD_NUMBER"
  }
  public data object CardApprovalNumber : PaymentTextSearchField {
    override val value: String = "CARD_APPROVAL_NUMBER"
  }
  public data object CardReceiptName : PaymentTextSearchField {
    override val value: String = "CARD_RECEIPT_NAME"
  }
  public data object CardInstallment : PaymentTextSearchField {
    override val value: String = "CARD_INSTALLMENT"
  }
  public data object TransBank : PaymentTextSearchField {
    override val value: String = "TRANS_BANK"
  }
  public data object VirtualAccountHolderName : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_HOLDER_NAME"
  }
  public data object VirtualAccountBank : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_BANK"
  }
  public data object VirtualAccountNumber : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_NUMBER"
  }
  public data object PgMerchantId : PaymentTextSearchField {
    override val value: String = "PG_MERCHANT_ID"
  }
  public data object PgTxId : PaymentTextSearchField {
    override val value: String = "PG_TX_ID"
  }
  public data object PgReceiptId : PaymentTextSearchField {
    override val value: String = "PG_RECEIPT_ID"
  }
  public data object ReceiptApprovalNumber : PaymentTextSearchField {
    override val value: String = "RECEIPT_APPROVAL_NUMBER"
  }
  public data object PgCancellationId : PaymentTextSearchField {
    override val value: String = "PG_CANCELLATION_ID"
  }
  public data object CancelReason : PaymentTextSearchField {
    override val value: String = "CANCEL_REASON"
  }
  public data object OrderName : PaymentTextSearchField {
    override val value: String = "ORDER_NAME"
  }
  public data object CustomerName : PaymentTextSearchField {
    override val value: String = "CUSTOMER_NAME"
  }
  public data object CustomerEmail : PaymentTextSearchField {
    override val value: String = "CUSTOMER_EMAIL"
  }
  public data object CustomerPhoneNumber : PaymentTextSearchField {
    override val value: String = "CUSTOMER_PHONE_NUMBER"
  }
  public data object CustomerAddress : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ADDRESS"
  }
  public data object CustomerZipcode : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ZIPCODE"
  }
  public data object UserAgent : PaymentTextSearchField {
    override val value: String = "USER_AGENT"
  }
  public data object BillingKey : PaymentTextSearchField {
    override val value: String = "BILLING_KEY"
  }
  public data object PromotionId : PaymentTextSearchField {
    override val value: String = "PROMOTION_ID"
  }
  public data object GiftCertificationApprovalNumber : PaymentTextSearchField {
    override val value: String = "GIFT_CERTIFICATION_APPROVAL_NUMBER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentTextSearchField
}


private object PaymentTextSearchFieldSerializer : KSerializer<PaymentTextSearchField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentTextSearchField::class.java.canonicalName, PrimitiveKind.STRING)
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
