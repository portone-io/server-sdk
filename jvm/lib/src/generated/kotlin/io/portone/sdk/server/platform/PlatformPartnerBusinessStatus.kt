package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 파트너 사업자 상태 */
@Serializable
public enum class PlatformPartnerBusinessStatus {
  /** 인증 되지 않음 */
  NotVerified,
  /** 인증 실패 */
  VerifyFailed,
  /** 대응되는 사업자 없음 */
  NotFound,
  /** 인증 대기 중 */
  Verifying,
  /** 사업 중 */
  InBusiness,
  /** 폐업 */
  Closed,
  /** 휴업 */
  Suspended,
}
