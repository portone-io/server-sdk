package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 사업자 상태 */
@Serializable(PlatformPartnerBusinessStatusSerializer::class)
public sealed interface PlatformPartnerBusinessStatus {
  public val value: String
  /** 인증 되지 않음 */
  public data object NotVerified : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_VERIFIED"
  }
  /** 인증 실패 */
  public data object VerifyFailed : PlatformPartnerBusinessStatus {
    override val value: String = "VERIFY_FAILED"
  }
  /** 대응되는 사업자 없음 */
  public data object NotFound : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_FOUND"
  }
  /** 인증 대기 중 */
  public data object Verifying : PlatformPartnerBusinessStatus {
    override val value: String = "VERIFYING"
  }
  /** 사업 중 */
  public data object InBusiness : PlatformPartnerBusinessStatus {
    override val value: String = "IN_BUSINESS"
  }
  /** 폐업 */
  public data object Closed : PlatformPartnerBusinessStatus {
    override val value: String = "CLOSED"
  }
  /** 휴업 */
  public data object Suspended : PlatformPartnerBusinessStatus {
    override val value: String = "SUSPENDED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerBusinessStatus
}


private object PlatformPartnerBusinessStatusSerializer : KSerializer<PlatformPartnerBusinessStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerBusinessStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerBusinessStatus {
    val value = decoder.decodeString()
    return when (value) {
      "NOT_VERIFIED" -> PlatformPartnerBusinessStatus.NotVerified
      "VERIFY_FAILED" -> PlatformPartnerBusinessStatus.VerifyFailed
      "NOT_FOUND" -> PlatformPartnerBusinessStatus.NotFound
      "VERIFYING" -> PlatformPartnerBusinessStatus.Verifying
      "IN_BUSINESS" -> PlatformPartnerBusinessStatus.InBusiness
      "CLOSED" -> PlatformPartnerBusinessStatus.Closed
      "SUSPENDED" -> PlatformPartnerBusinessStatus.Suspended
      else -> PlatformPartnerBusinessStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerBusinessStatus) = encoder.encodeString(value.value)
}
