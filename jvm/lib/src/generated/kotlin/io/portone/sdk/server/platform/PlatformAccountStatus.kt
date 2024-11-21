package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 계좌 상태 */
@Serializable
public sealed interface PlatformAccountStatus {
  public val value: String
  /** 계좌 인증 완료됨 */
  @SerialName("VERIFIED")
  public data object Verified : PlatformAccountStatus {
    override val value: String = "VERIFIED"
  }
  /** 계좌주 불일치 */
  @SerialName("VERIFY_FAILED")
  public data object VerifyFailed : PlatformAccountStatus {
    override val value: String = "VERIFY_FAILED"
  }
  /** 계좌 인증 오류 */
  @SerialName("VERIFY_ERROR")
  public data object VerifyError : PlatformAccountStatus {
    override val value: String = "VERIFY_ERROR"
  }
  /** 계좌 인증 안됨 */
  @SerialName("NOT_VERIFIED")
  public data object NotVerified : PlatformAccountStatus {
    override val value: String = "NOT_VERIFIED"
  }
  /** 알 수 없는 상태 */
  @SerialName("UNKNOWN")
  public data object Unknown : PlatformAccountStatus {
    override val value: String = "UNKNOWN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountStatus
}
