package io.portone.sdk.server.payment.cashreceipt

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 발급 시 고객 식별 정보 유형 */
@Serializable(IssueCashReceiptCustomerInputIdentityNumberTypeSerializer::class)
public sealed interface IssueCashReceiptCustomerInputIdentityNumberType {
  public val value: String
  /** 휴대전화번호 */
  @Serializable(PhoneSerializer::class)
  public data object Phone : IssueCashReceiptCustomerInputIdentityNumberType {
    override val value: String = "PHONE"
  }
  private object PhoneSerializer : KSerializer<Phone> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Phone::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Phone = decoder.decodeString().let {
      if (it != "PHONE") {
        throw SerializationException(it)
      } else {
        return Phone
      }
    }
    override fun serialize(encoder: Encoder, value: Phone) = encoder.encodeString(value.value)
  }
  /** 카드번호 */
  @Serializable(CardSerializer::class)
  public data object Card : IssueCashReceiptCustomerInputIdentityNumberType {
    override val value: String = "CARD"
  }
  private object CardSerializer : KSerializer<Card> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Card::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Card = decoder.decodeString().let {
      if (it != "CARD") {
        throw SerializationException(it)
      } else {
        return Card
      }
    }
    override fun serialize(encoder: Encoder, value: Card) = encoder.encodeString(value.value)
  }
  /** 사업자등록번호 */
  @Serializable(BusinessSerializer::class)
  public data object Business : IssueCashReceiptCustomerInputIdentityNumberType {
    override val value: String = "BUSINESS"
  }
  private object BusinessSerializer : KSerializer<Business> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Business::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Business = decoder.decodeString().let {
      if (it != "BUSINESS") {
        throw SerializationException(it)
      } else {
        return Business
      }
    }
    override fun serialize(encoder: Encoder, value: Business) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IssueCashReceiptCustomerInputIdentityNumberType
}


private object IssueCashReceiptCustomerInputIdentityNumberTypeSerializer : KSerializer<IssueCashReceiptCustomerInputIdentityNumberType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssueCashReceiptCustomerInputIdentityNumberType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IssueCashReceiptCustomerInputIdentityNumberType {
    val value = decoder.decodeString()
    return when (value) {
      "PHONE" -> IssueCashReceiptCustomerInputIdentityNumberType.Phone
      "CARD" -> IssueCashReceiptCustomerInputIdentityNumberType.Card
      "BUSINESS" -> IssueCashReceiptCustomerInputIdentityNumberType.Business
      else -> IssueCashReceiptCustomerInputIdentityNumberType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IssueCashReceiptCustomerInputIdentityNumberType) = encoder.encodeString(value.value)
}
