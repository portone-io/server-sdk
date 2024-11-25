package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 상태 */
@Serializable(PlatformPartnerStatusSerializer::class)
public sealed interface PlatformPartnerStatus {
  public val value: String
  /** 승인 대기 중 */
  public data object Pending : PlatformPartnerStatus {
    override val value: String = "PENDING"
  }
  /** 승인 완료 */
  public data object Approved : PlatformPartnerStatus {
    override val value: String = "APPROVED"
  }
  /** 승인 거절 */
  public data object Rejected : PlatformPartnerStatus {
    override val value: String = "REJECTED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerStatus
}


private object PlatformPartnerStatusSerializer : KSerializer<PlatformPartnerStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PENDING" -> PlatformPartnerStatus.Pending
      "APPROVED" -> PlatformPartnerStatus.Approved
      "REJECTED" -> PlatformPartnerStatus.Rejected
      else -> PlatformPartnerStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerStatus) = encoder.encodeString(value.value)
}
