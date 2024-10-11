package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 계좌 상태 */
@Serializable
public enum class PlatformAccountStatus {
  /** 계좌 인증 중 */
  VERIFYING,
  /** 계좌 인증 완료됨 */
  VERIFIED,
  /** 계좌 인증 실패함 */
  VERIFY_FAILED,
  /** 계좌 인증 안됨 */
  NOT_VERIFIED,
  /** 계좌 인증 만료됨 */
  EXPIRED,
  /** 알 수 없는 상태 */
  UNKNOWN,
}
