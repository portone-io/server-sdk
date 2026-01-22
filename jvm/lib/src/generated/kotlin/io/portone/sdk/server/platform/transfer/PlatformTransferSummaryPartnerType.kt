package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 파트너 유형 */
@Serializable(PlatformTransferSummaryPartnerTypeSerializer::class)
public sealed interface PlatformTransferSummaryPartnerType {
  public val value: String
  /** 사업자 */
  @Serializable(BusinessSerializer::class)
  public data object Business : PlatformTransferSummaryPartnerType {
    override val value: String = "BUSINESS"
  }
  public object BusinessSerializer : KSerializer<Business> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Business::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Business = decoder.decodeString().let {
      if (it != "BUSINESS") {
        throw SerializationException(it)
      } else {
        return Business
      }
    }
    override fun serialize(encoder: Encoder, value: Business): Unit = encoder.encodeString(value.value)
  }
  /** 원천징수 대상자 */
  @Serializable(WhtPayerSerializer::class)
  public data object WhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "WHT_PAYER"
  }
  public object WhtPayerSerializer : KSerializer<WhtPayer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WhtPayer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WhtPayer = decoder.decodeString().let {
      if (it != "WHT_PAYER") {
        throw SerializationException(it)
      } else {
        return WhtPayer
      }
    }
    override fun serialize(encoder: Encoder, value: WhtPayer): Unit = encoder.encodeString(value.value)
  }
  /** 원천징수 비대상자 */
  @Serializable(NonWhtPayerSerializer::class)
  public data object NonWhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "NON_WHT_PAYER"
  }
  public object NonWhtPayerSerializer : KSerializer<NonWhtPayer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NonWhtPayer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NonWhtPayer = decoder.decodeString().let {
      if (it != "NON_WHT_PAYER") {
        throw SerializationException(it)
      } else {
        return NonWhtPayer
      }
    }
    override fun serialize(encoder: Encoder, value: NonWhtPayer): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferSummaryPartnerType
}


public object PlatformTransferSummaryPartnerTypeSerializer : KSerializer<PlatformTransferSummaryPartnerType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferSummaryPartnerType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferSummaryPartnerType {
    val value = decoder.decodeString()
    return when (value) {
      "BUSINESS" -> PlatformTransferSummaryPartnerType.Business
      "WHT_PAYER" -> PlatformTransferSummaryPartnerType.WhtPayer
      "NON_WHT_PAYER" -> PlatformTransferSummaryPartnerType.NonWhtPayer
      else -> PlatformTransferSummaryPartnerType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferSummaryPartnerType): Unit = encoder.encodeString(value.value)
}
