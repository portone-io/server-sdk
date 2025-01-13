package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PromotionDiscountRetainOptionSerializer::class)
public sealed interface PromotionDiscountRetainOption {
  public val value: String
  @Serializable(RetainSerializer::class)
  public data object Retain : PromotionDiscountRetainOption {
    override val value: String = "RETAIN"
  }
  private object RetainSerializer : KSerializer<Retain> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Retain::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Retain = decoder.decodeString().let {
      if (it != "RETAIN") {
        throw SerializationException(it)
      } else {
        return Retain
      }
    }
    override fun serialize(encoder: Encoder, value: Retain) = encoder.encodeString(value.value)
  }
  @Serializable(ReleaseSerializer::class)
  public data object Release : PromotionDiscountRetainOption {
    override val value: String = "RELEASE"
  }
  private object ReleaseSerializer : KSerializer<Release> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Release::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Release = decoder.decodeString().let {
      if (it != "RELEASE") {
        throw SerializationException(it)
      } else {
        return Release
      }
    }
    override fun serialize(encoder: Encoder, value: Release) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionDiscountRetainOption
}


private object PromotionDiscountRetainOptionSerializer : KSerializer<PromotionDiscountRetainOption> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PromotionDiscountRetainOption::class.java.name, PrimitiveKind.STRING)
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
