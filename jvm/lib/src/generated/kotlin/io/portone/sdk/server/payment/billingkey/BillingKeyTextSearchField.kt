package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통합검색 항목 */
@Serializable(BillingKeyTextSearchFieldSerializer::class)
public sealed interface BillingKeyTextSearchField {
  public val value: String
  @Serializable(CardBinSerializer::class)
  public data object CardBin : BillingKeyTextSearchField {
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
  public data object CardNumber : BillingKeyTextSearchField {
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
  @Serializable(PgMerchantIdSerializer::class)
  public data object PgMerchantId : BillingKeyTextSearchField {
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
  @Serializable(CustomerNameSerializer::class)
  public data object CustomerName : BillingKeyTextSearchField {
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
  public data object CustomerEmail : BillingKeyTextSearchField {
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
  public data object CustomerPhoneNumber : BillingKeyTextSearchField {
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
  public data object CustomerAddress : BillingKeyTextSearchField {
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
  public data object CustomerZipcode : BillingKeyTextSearchField {
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
  public data object UserAgent : BillingKeyTextSearchField {
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
  public data object BillingKey : BillingKeyTextSearchField {
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
  @Serializable(ChannelGroupNameSerializer::class)
  public data object ChannelGroupName : BillingKeyTextSearchField {
    override val value: String = "CHANNEL_GROUP_NAME"
  }
  private object ChannelGroupNameSerializer : KSerializer<ChannelGroupName> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ChannelGroupName::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ChannelGroupName = decoder.decodeString().let {
      if (it != "CHANNEL_GROUP_NAME") {
        throw SerializationException(it)
      } else {
        return ChannelGroupName
      }
    }
    override fun serialize(encoder: Encoder, value: ChannelGroupName) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyTextSearchField
}


private object BillingKeyTextSearchFieldSerializer : KSerializer<BillingKeyTextSearchField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyTextSearchField::class.java.name, PrimitiveKind.STRING)
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
