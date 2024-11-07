package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 계좌 상태 */
@Serializable
public enum class PlatformAccountStatus {
  /** 계좌 인증 중 */
  Verifying,
  /** 계좌 인증 완료됨 */
  Verified,
  /** 계좌 인증 실패함 */
  VerifyFailed,
  /** 계좌 인증 안됨 */
  NotVerified,
  /** 계좌 인증 만료됨 */
  Expired,
  /** 알 수 없는 상태 */
  Unknown,
}
