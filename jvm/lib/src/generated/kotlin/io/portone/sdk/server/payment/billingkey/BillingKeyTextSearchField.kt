package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통합검색 항목 */
@Serializable(BillingKeyTextSearchFieldSerializer::class)
public sealed interface BillingKeyTextSearchField {
  public val value: String
  public data object CardBin : BillingKeyTextSearchField {
    override val value: String = "CARD_BIN"
  }
  public data object CardNumber : BillingKeyTextSearchField {
    override val value: String = "CARD_NUMBER"
  }
  public data object PgMerchantId : BillingKeyTextSearchField {
    override val value: String = "PG_MERCHANT_ID"
  }
  public data object CustomerName : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_NAME"
  }
  public data object CustomerEmail : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_EMAIL"
  }
  public data object CustomerPhoneNumber : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_PHONE_NUMBER"
  }
  public data object CustomerAddress : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_ADDRESS"
  }
  public data object CustomerZipcode : BillingKeyTextSearchField {
    override val value: String = "CUSTOMER_ZIPCODE"
  }
  public data object UserAgent : BillingKeyTextSearchField {
    override val value: String = "USER_AGENT"
  }
  public data object BillingKey : BillingKeyTextSearchField {
    override val value: String = "BILLING_KEY"
  }
  public data object ChannelGroupName : BillingKeyTextSearchField {
    override val value: String = "CHANNEL_GROUP_NAME"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyTextSearchField
}


private object BillingKeyTextSearchFieldSerializer : KSerializer<BillingKeyTextSearchField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyTextSearchField::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeyTextSearchField {
    val value = decoder.decodeString()
    return when (value) {
      "CARD_BIN" -> BillingKeyTextSearchField.CardBin
      "CARD_NUMBER" -> BillingKeyTextSearchField.CardNumber
      "PG_MERCHANT_ID" -> BillingKeyTextSearchField.PgMerchantId
      "CUSTOMER_NAME" -> BillingKeyTextSearchField.CustomerName
      "CUSTOMER_EMAIL" -> BillingKeyTextSearchField.CustomerEmail
      "CUSTOMER_PHONE_NUMBER" -> BillingKeyTextSearchField.CustomerPhoneNumber
      "CUSTOMER_ADDRESS" -> BillingKeyTextSearchField.CustomerAddress
      "CUSTOMER_ZIPCODE" -> BillingKeyTextSearchField.CustomerZipcode
      "USER_AGENT" -> BillingKeyTextSearchField.UserAgent
      "BILLING_KEY" -> BillingKeyTextSearchField.BillingKey
      "CHANNEL_GROUP_NAME" -> BillingKeyTextSearchField.ChannelGroupName
      else -> BillingKeyTextSearchField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeyTextSearchField) = encoder.encodeString(value.value)
}
