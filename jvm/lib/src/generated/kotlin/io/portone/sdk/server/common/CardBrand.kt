package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 카드 브랜드 */
@Serializable(CardBrandSerializer::class)
public sealed interface CardBrand {
  public val value: String
  public data object Local : CardBrand {
    override val value: String = "LOCAL"
  }
  public data object Master : CardBrand {
    override val value: String = "MASTER"
  }
  public data object Unionpay : CardBrand {
    override val value: String = "UNIONPAY"
  }
  public data object Visa : CardBrand {
    override val value: String = "VISA"
  }
  public data object Jcb : CardBrand {
    override val value: String = "JCB"
  }
  public data object Amex : CardBrand {
    override val value: String = "AMEX"
  }
  public data object Diners : CardBrand {
    override val value: String = "DINERS"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardBrand
}


private object CardBrandSerializer : KSerializer<CardBrand> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardBrand::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CardBrand {
    val value = decoder.decodeString()
    return when (value) {
      "LOCAL" -> CardBrand.Local
      "MASTER" -> CardBrand.Master
      "UNIONPAY" -> CardBrand.Unionpay
      "VISA" -> CardBrand.Visa
      "JCB" -> CardBrand.Jcb
      "AMEX" -> CardBrand.Amex
      "DINERS" -> CardBrand.Diners
      else -> CardBrand.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CardBrand) = encoder.encodeString(value.value)
}
