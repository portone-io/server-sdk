package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 파트너 사업자 상태 */
@Serializable
public enum class PlatformPartnerBusinessStatus {
  /** 인증 되지 않음 */
  NOT_VERIFIED,
  /** 인증 실패 */
  VERIFY_FAILED,
  /** 대응되는 사업자 없음 */
  NOT_FOUND,
  /** 인증 대기 중 */
  VERIFYING,
  /** 사업 중 */
  IN_BUSINESS,
  /** 폐업 */
  CLOSED,
  /** 휴업 */
  SUSPENDED,
}
