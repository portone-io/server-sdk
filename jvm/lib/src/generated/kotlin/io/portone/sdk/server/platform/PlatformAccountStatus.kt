package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 계좌 상태 */
@Serializable
public sealed class PlatformAccountStatus {
  /** 계좌 인증 완료됨 */
  @SerialName("VERIFIED")
  public data object Verified : PlatformAccountStatus()
  /** 계좌주 불일치 */
  @SerialName("VERIFY_FAILED")
  public data object VerifyFailed : PlatformAccountStatus()
  /** 계좌 인증 오류 */
  @SerialName("VERIFY_ERROR")
  public data object VerifyError : PlatformAccountStatus()
  /** 계좌 인증 안됨 */
  @SerialName("NOT_VERIFIED")
  public data object NotVerified : PlatformAccountStatus()
  /** 알 수 없는 상태 */
  @SerialName("UNKNOWN")
  public data object Unknown : PlatformAccountStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformAccountStatus()
}
