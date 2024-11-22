package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Business : PlatformTransferSummaryPartnerType {
    override val value: String = "BUSINESS"
  }
  /** 원천징수 대상자 */
  public data object WhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "WHT_PAYER"
  }
  /** 원천징수 비대상자 */
  public data object NonWhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "NON_WHT_PAYER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferSummaryPartnerType
}


private object PlatformTransferSummaryPartnerTypeSerializer : KSerializer<PlatformTransferSummaryPartnerType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferSummaryPartnerType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferSummaryPartnerType {
    val value = decoder.decodeString()
    return when (value) {
      "BUSINESS" -> PlatformTransferSummaryPartnerType.Business
      "WHT_PAYER" -> PlatformTransferSummaryPartnerType.WhtPayer
      "NON_WHT_PAYER" -> PlatformTransferSummaryPartnerType.NonWhtPayer
      else -> PlatformTransferSummaryPartnerType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferSummaryPartnerType) = encoder.encodeString(value.value)
}
