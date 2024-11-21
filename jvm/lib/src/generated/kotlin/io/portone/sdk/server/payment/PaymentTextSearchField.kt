package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 통합검색 항목 */
@Serializable
public sealed interface PaymentTextSearchField {
  public val value: String
  @SerialName("ALL")
  public data object All : PaymentTextSearchField {
    override val value: String = "ALL"
  }
  @SerialName("PAYMENT_ID")
  public data object PaymentId : PaymentTextSearchField {
    override val value: String = "PAYMENT_ID"
  }
  @SerialName("TX_ID")
  public data object TxId : PaymentTextSearchField {
    override val value: String = "TX_ID"
  }
  @SerialName("SCHEDULE_ID")
  public data object ScheduleId : PaymentTextSearchField {
    override val value: String = "SCHEDULE_ID"
  }
  @SerialName("FAIL_REASON")
  public data object FailReason : PaymentTextSearchField {
    override val value: String = "FAIL_REASON"
  }
  @SerialName("CARD_ISSUER")
  public data object CardIssuer : PaymentTextSearchField {
    override val value: String = "CARD_ISSUER"
  }
  @SerialName("CARD_ACQUIRER")
  public data object CardAcquirer : PaymentTextSearchField {
    override val value: String = "CARD_ACQUIRER"
  }
  @SerialName("CARD_BIN")
  public data object CardBin : PaymentTextSearchField {
    override val value: String = "CARD_BIN"
  }
  @SerialName("CARD_NUMBER")
  public data object CardNumber : PaymentTextSearchField {
    override val value: String = "CARD_NUMBER"
  }
  @SerialName("CARD_APPROVAL_NUMBER")
  public data object CardApprovalNumber : PaymentTextSearchField {
    override val value: String = "CARD_APPROVAL_NUMBER"
  }
  @SerialName("CARD_RECEIPT_NAME")
  public data object CardReceiptName : PaymentTextSearchField {
    override val value: String = "CARD_RECEIPT_NAME"
  }
  @SerialName("CARD_INSTALLMENT")
  public data object CardInstallment : PaymentTextSearchField {
    override val value: String = "CARD_INSTALLMENT"
  }
  @SerialName("TRANS_BANK")
  public data object TransBank : PaymentTextSearchField {
    override val value: String = "TRANS_BANK"
  }
  @SerialName("VIRTUAL_ACCOUNT_HOLDER_NAME")
  public data object VirtualAccountHolderName : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_HOLDER_NAME"
  }
  @SerialName("VIRTUAL_ACCOUNT_BANK")
  public data object VirtualAccountBank : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_BANK"
  }
  @SerialName("VIRTUAL_ACCOUNT_NUMBER")
  public data object VirtualAccountNumber : PaymentTextSearchField {
    override val value: String = "VIRTUAL_ACCOUNT_NUMBER"
  }
  @SerialName("PG_MERCHANT_ID")
  public data object PgMerchantId : PaymentTextSearchField {
    override val value: String = "PG_MERCHANT_ID"
  }
  @SerialName("PG_TX_ID")
  public data object PgTxId : PaymentTextSearchField {
    override val value: String = "PG_TX_ID"
  }
  @SerialName("PG_RECEIPT_ID")
  public data object PgReceiptId : PaymentTextSearchField {
    override val value: String = "PG_RECEIPT_ID"
  }
  @SerialName("RECEIPT_APPROVAL_NUMBER")
  public data object ReceiptApprovalNumber : PaymentTextSearchField {
    override val value: String = "RECEIPT_APPROVAL_NUMBER"
  }
  @SerialName("PG_CANCELLATION_ID")
  public data object PgCancellationId : PaymentTextSearchField {
    override val value: String = "PG_CANCELLATION_ID"
  }
  @SerialName("CANCEL_REASON")
  public data object CancelReason : PaymentTextSearchField {
    override val value: String = "CANCEL_REASON"
  }
  @SerialName("ORDER_NAME")
  public data object OrderName : PaymentTextSearchField {
    override val value: String = "ORDER_NAME"
  }
  @SerialName("CUSTOMER_NAME")
  public data object CustomerName : PaymentTextSearchField {
    override val value: String = "CUSTOMER_NAME"
  }
  @SerialName("CUSTOMER_EMAIL")
  public data object CustomerEmail : PaymentTextSearchField {
    override val value: String = "CUSTOMER_EMAIL"
  }
  @SerialName("CUSTOMER_PHONE_NUMBER")
  public data object CustomerPhoneNumber : PaymentTextSearchField {
    override val value: String = "CUSTOMER_PHONE_NUMBER"
  }
  @SerialName("CUSTOMER_ADDRESS")
  public data object CustomerAddress : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ADDRESS"
  }
  @SerialName("CUSTOMER_ZIPCODE")
  public data object CustomerZipcode : PaymentTextSearchField {
    override val value: String = "CUSTOMER_ZIPCODE"
  }
  @SerialName("USER_AGENT")
  public data object UserAgent : PaymentTextSearchField {
    override val value: String = "USER_AGENT"
  }
  @SerialName("BILLING_KEY")
  public data object BillingKey : PaymentTextSearchField {
    override val value: String = "BILLING_KEY"
  }
  @SerialName("PROMOTION_ID")
  public data object PromotionId : PaymentTextSearchField {
    override val value: String = "PROMOTION_ID"
  }
  @SerialName("GIFT_CERTIFICATION_APPROVAL_NUMBER")
  public data object GiftCertificationApprovalNumber : PaymentTextSearchField {
    override val value: String = "GIFT_CERTIFICATION_APPROVAL_NUMBER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentTextSearchField
}
