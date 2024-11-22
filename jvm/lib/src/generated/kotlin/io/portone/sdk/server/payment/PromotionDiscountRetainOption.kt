package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PromotionDiscountRetainOptionSerializer::class)
public sealed interface PromotionDiscountRetainOption {
  public val value: String
  public data object Retain : PromotionDiscountRetainOption {
    override val value: String = "RETAIN"
  }
  public data object Release : PromotionDiscountRetainOption {
    override val value: String = "RELEASE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionDiscountRetainOption
}


private object PromotionDiscountRetainOptionSerializer : KSerializer<PromotionDiscountRetainOption> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionDiscountRetainOption::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PromotionDiscountRetainOption {
    val value = decoder.decodeString()
    return when (value) {
      "RETAIN" -> PromotionDiscountRetainOption.Retain
      "RELEASE" -> PromotionDiscountRetainOption.Release
      else -> PromotionDiscountRetainOption.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PromotionDiscountRetainOption) = encoder.encodeString(value.value)
}
