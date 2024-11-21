package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 통합검색 항목 */
@Serializable
public sealed interface BillingKeyTextSearchField {
  public val value: String
  @SerialName("CARD_BIN")
  public data object CardBin : BillingKeyTextSearchField {
    override val value: String = "CARD_BIN"
  }
  @SerialName("CARD_NUMBER")
  public data object CardNumber : BillingKeyTextSearchField {
    override val value: String = "CARD_NUMBER"
  }
  @SerialName("PG_MERCHANT_ID")
  public data object PgMerchantId : BillingKeyTextSearchField {
    override val value: String = "PG_MERCHANT_ID"
  }
  @SerialName("CUSTOMER_NAME")
  public data object CustomerName : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_NAME"
  }
  @SerialName("CUSTOMER_EMAIL")
  public data object CustomerEmail : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_EMAIL"
  }
  @SerialName("CUSTOMER_PHONE_NUMBER")
  public data object CustomerPhoneNumber : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_PHONE_NUMBER"
  }
  @SerialName("CUSTOMER_ADDRESS")
  public data object CustomerAddress : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_ADDRESS"
  }
  @SerialName("CUSTOMER_ZIPCODE")
  public data object CustomerZipcode : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_ZIPCODE"
  }
  @SerialName("USER_AGENT")
  public data object UserAgent : BillingKeyTextSearchField {
    override val value: String = "USER_AGENT"
  }
  @SerialName("BILLING_KEY")
  public data object BillingKey : BillingKeyTextSearchField {
    override val value: String = "BILLING_KEY"
  }
  @SerialName("CHANNEL_GROUP_NAME")
  public data object ChannelGroupName : BillingKeyTextSearchField {
    override val value: String = "CHANNEL_GROUP_NAME"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyTextSearchField
}
