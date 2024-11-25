package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 계좌 상태 */
@Serializable(PlatformAccountStatusSerializer::class)
public sealed interface PlatformAccountStatus {
  public val value: String
  /** 계좌 인증 완료됨 */
  public data object Verified : PlatformAccountStatus {
    override val value: String = "VERIFIED"
  }
  /** 계좌주 불일치 */
  public data object VerifyFailed : PlatformAccountStatus {
    override val value: String = "VERIFY_FAILED"
  }
  /** 계좌 인증 오류 */
  public data object VerifyError : PlatformAccountStatus {
    override val value: String = "VERIFY_ERROR"
  }
  /** 계좌 인증 안됨 */
  public data object NotVerified : PlatformAccountStatus {
    override val value: String = "NOT_VERIFIED"
  }
  /** 알 수 없는 상태 */
  public data object Unknown : PlatformAccountStatus {
    override val value: String = "UNKNOWN"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountStatus
}


private object PlatformAccountStatusSerializer : KSerializer<PlatformAccountStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountStatus {
    val value = decoder.decodeString()
    return when (value) {
      "VERIFIED" -> PlatformAccountStatus.Verified
      "VERIFY_FAILED" -> PlatformAccountStatus.VerifyFailed
      "VERIFY_ERROR" -> PlatformAccountStatus.VerifyError
      "NOT_VERIFIED" -> PlatformAccountStatus.NotVerified
      "UNKNOWN" -> PlatformAccountStatus.Unknown
      else -> PlatformAccountStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountStatus) = encoder.encodeString(value.value)
}
