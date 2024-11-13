package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 통합검색 항목 */
@Serializable
public sealed class BillingKeyTextSearchField {
  @SerialName("CARD_BIN")
  public data object CardBin : BillingKeyTextSearchField()
  @SerialName("CARD_NUMBER")
  public data object CardNumber : BillingKeyTextSearchField()
  @SerialName("PG_MERCHANT_ID")
  public data object PgMerchantId : BillingKeyTextSearchField()
  @SerialName("CUSTOMER_NAME")
  public data object CustomerName : BillingKeyTextSearchField()
  @SerialName("CUSTOMER_EMAIL")
  public data object CustomerEmail : BillingKeyTextSearchField()
  @SerialName("CUSTOMER_PHONE_NUMBER")
  public data object CustomerPhoneNumber : BillingKeyTextSearchField()
  @SerialName("CUSTOMER_ADDRESS")
  public data object CustomerAddress : BillingKeyTextSearchField()
  @SerialName("CUSTOMER_ZIPCODE")
  public data object CustomerZipcode : BillingKeyTextSearchField()
  @SerialName("USER_AGENT")
  public data object UserAgent : BillingKeyTextSearchField()
  @SerialName("BILLING_KEY")
  public data object BillingKey : BillingKeyTextSearchField()
  @SerialName("CHANNEL_GROUP_NAME")
  public data object ChannelGroupName : BillingKeyTextSearchField()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : BillingKeyTextSearchField()
}
